# gpapconv

Geopaparazzi to OSM XML and GeoJSON converter

Demo: https://gpapconv.frafra.eu/

## Dependencies

- [Python 3](https://www.python.org/)
  - [hug](http://www.hug.rest/)
  - [uWSGI](https://uwsgi-docs.readthedocs.io/)
- [sqlite](https://sqlite.org/)

## Setup

### uwsgi

```
$ uwsgi --ini uwsgi.ini
```

### Docker image

```
$ docker build --tag=gpapconv .
$ docker run --publish 8000:8000 --detach gpapconv
```

## How to use

### Web interface

Open http://localhost:8000.

### Command line interface

From gpap to OSM XML:

```
$ curl -X POST -F "file=@geopaparazzi.gpap" http://localhost:8000/gpap2osm
```

From gpap to OSM GeoJSON:

```
$ curl -X POST -F "file=@geopaparazzi.gpap" http://localhost:8000/gpap2geojson
```
