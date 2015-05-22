# Reference
# https://www.youtube.com/watch?v=aIX2ZrSWgnc

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='mill', llcrnrlat=-60, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180, resolution='c')

m.drawcoastlines()
# m.drawcountries()
# m.drawstates()
# m.drawrivers()
# m.fillcontinents(color='#04BAE3', lake_color='#FFFFFF')

m.drawmapboundary(fill_color='#FFFFFF')
m.bluemarble()
plt.title('Quick basemap example')
plt.show()
