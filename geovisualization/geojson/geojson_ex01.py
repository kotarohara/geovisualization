import json
import pprint as pp

# Data from https://www.mapbox.com/mapbox.js/example/v1.0.0/load-geojson/
with open('../data/geojson/ex01.geojson') as f:
    data = json.load(f)

pp.pprint(data)