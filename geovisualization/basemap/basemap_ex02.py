# Reference
# https://www.youtube.com/watch?v=KpS0uEFkfHg

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# m = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90,
#             llcrnrlon=-180, urcrnrlon=180, resolution='c')
m = Basemap(projection='mill', llcrnrlat=-60, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180, resolution='c')

m.drawcoastlines()
m.fillcontinents(color='#072b57', lake_color='#FFFFFF')

m.drawmapboundary(fill_color='#FFFFFF')
plt.title('Quick basemap example')
plt.show()
