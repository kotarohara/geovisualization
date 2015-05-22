"""
Code from https://gist.github.com/urschrei/6436526
Written by urschrei

required packages:
numpy
matplotlib
basemap: http://matplotlib.org/basemap/users/installing.html
shapely: https://pypi.python.org/pypi/Shapely
descartes: https://pypi.python.org/pypi/descartes
random


numpy and random are only required to generate random points for this example

"""

from random import shuffle, randint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from mpl_toolkits.basemap import Basemap
from shapely.geometry import Point, MultiPoint, MultiPolygon
from descartes import PolygonPatch


# lower left minx miny , upper right maxx maxy
bounds = [-6.108398, 49.61071, 1.669922, 58.972667]
minx, miny, maxx, maxy = bounds
w, h = maxx - minx, maxy - miny

# generate random points within the bounds
lon = np.linspace(minx, maxx).tolist()
lat = np.linspace(miny, maxy).tolist()
shuffle(lon)
shuffle(lat)

# create a new matplotlib figure and axes instance
fig = plt.figure()
ax = fig.add_subplot(111)
# add a basemap and a small additional extent
m = Basemap(
    projection='merc',
    ellps = 'WGS84',
    llcrnrlon=minx - 0.2 * w,
    llcrnrlat=miny - 0.2 * h,
    urcrnrlon=maxx + 0.2 * w,
    urcrnrlat=maxy + 0.2 * h,
    lat_ts=0,
    resolution='h')
m.drawcoastlines(linewidth=0.3)
m.drawmapboundary()
# a shapefile can be added like so if needed
# m.readshapefile('london_shp', 'london', color='#555555')

# set axes limits to basemap's coordinate reference system
min_x, min_y = m(minx, miny)
max_x, max_y = m(maxx, maxy)
corr_w, corr_h = max_x - min_x, max_y - min_y
ax.set_xlim(min_x - 0.2 * corr_w, max_x + 0.2 * corr_w)
ax.set_ylim(min_y - 0.2 * corr_h, max_y + 0.2 * corr_h)
# square up axes and basemap
ax.set_aspect(1)
# buffer units are translated to metres by Basemap
# we're randomly varying between 7.5k and 15k metres
patches = [PolygonPatch(Point(m(lon, lat)).buffer(1.0 * randint(7500, 15000)),
                        fc='#cc00cc', ec='#555555', alpha=0.5, zorder=4)
           for lon, lat in zip(lon, lat)]

ax.add_collection(PatchCollection(patches, match_original=True))
plt.savefig('../data/uk.png', dpi=300)
plt.show()