from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import json
import pprint as pp

# Data from http://eric.clst.org/Stuff/USGeoJSON
with open('../data/geojson/gz_2010_us_outline_500k.json') as f:
    data = json.load(f)

m = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')
m.drawcoastlines()
m.fillcontinents()


for feature in data['features']:
    points = np.array(feature['geometry']['coordinates'])
    x, y = m(points[:, 0], points[:, 1])
    m.plot(x, y, color="red", linestyle='-', linewidth=3, alpha=.5)
    # m.plot(x, y, color="#000000", marker='o', markersize=4, alpha=.5)


plt.title('Quick basemap example')
plt.show()


