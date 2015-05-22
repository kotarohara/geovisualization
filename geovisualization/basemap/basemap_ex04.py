# Reference
# https://www.youtube.com/watch?v=Xr6sG1QnMbw

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='mill', llcrnrlat=20, urcrnrlat=50,
            llcrnrlon=-130, urcrnrlon=-60, resolution='c')

m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.fillcontinents(color='#04BAE3', lake_color='#FFFFFF')
m.drawmapboundary(fill_color='#FFFFFF')

lat, lon = 29.76, -95.36
x, y = m(lon, lat)
m.plot(x, y, 'ro')

lat, lon = 40.12, -104.24
x, y = m(lon, lat)
m.plot(x, y, 'go')

plt.title('Geo Plotting')
plt.show()
