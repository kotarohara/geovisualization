# Reference
# https://www.youtube.com/watch?v=E6gvtfQHJUs

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')

m.drawcoastlines()
m.fillcontinents()

m.drawmapboundary()
plt.title('Quick basemap example')
plt.show()
