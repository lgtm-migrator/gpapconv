#!/usr/bin/env python3


from fastapi import FastAPI, File, UploadFile
from starlette.responses import Response
from starlette.staticfiles import StaticFiles

import anosql
import datetime
import json
import shutil
import sqlite3
import tempfile

queries = anosql.from_path('queries.sql', 'sqlite3')

def run_query_on_db(db_path, query_name):
    with sqlite3.connect(db_path) as con:
        return getattr(queries, query_name)(con)[0][0]

def run_query_on_form(file, query_name):
    with tempfile.NamedTemporaryFile() as tf:
        shutil.copyfileobj(file.file, tf)
        return run_query_on_db(tf.name, query_name)

def generate_filename(extension):
    return 'geopap-{}.{}'.format(datetime.date.today(), extension)

app = FastAPI()
app.mount("/", StaticFiles(directory="web"), name="web")

@app.post("/gpap2osm")
async def gpap2osm(response: Response, file: UploadFile = File(...)):
    response.headers['Content-Disposition'] = generate_filename('xml')
    result = run_query_on_form(file, 'gpap2osm')
    return Response(result, media_type="application/xml")

@app.post("/gpap2geojson")
async def gpap2geojson(response: Response, file: UploadFile = File(...)):
    response.headers['Content-Disposition'] = generate_filename('geojson')
    result = run_query_on_form(file, 'gpap2geojson')
    return json.loads(result)
