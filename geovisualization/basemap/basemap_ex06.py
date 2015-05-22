from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='mill', llcrnrlat=20, urcrnrlat=50,
            llcrnrlon=-130, urcrnrlon=-60, resolution='c')

m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.fillcontinents(color='#EEEEEE', lake_color='#FFFFFF')
m.drawmapboundary(fill_color='#FFFFFF')

lat = 30, 31, 34, 33, 32
lon = -103, -110, -107, -111, -115

# Plotting segments
# http://stackoverflow.com/questions/11603537/plot-multiple-lines-in-python-basemap
x, y = m(lon, lat)
m.plot(x, y, color="#000000", linestyle='-', linewidth=2, alpha=.5)
m.plot(x, y, color="#000000", marker='o', markersize=4, alpha=.5)

plt.title('Segment plotting')
plt.show()
