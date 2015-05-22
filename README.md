# Geovisualization

## Requirements
This project uses the following python libraries as well as the C/C++ libraries that they depend on.
* Basemap >= 1.0.7

I think, especially on Windows, the easiest way to go is to use 
Anaconda Python (https://store.continuum.io/cshop/anaconda/), a free Python distribution from Continuum.

To install requirements, just use the `conda` command (e.g., `conda install basemap`). Note, however, at 
the time of writing, GEOS (a C++ library for GIS stuff) cannot be installed on a Windows machine via
`conda`. So instead, I install it through OSGeo4W bundle (http://trac.osgeo.org/osgeo4w/).

Another hiccup I encountered with installing dependencies is installing Shapely. I don't know why, but the 
Shapely installed through `pip` cannot find the GEOS library. So I followed the instruction here: http://gis.stackexchange.com/questions/38899/geos-and-shapely-installation-on-windows

* Uninstall Shapely (`pip uninstall shapely`)
* Download the Shapely wheel file from the following link: http://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely
* Run `pip install wheel`
* Run `pip install THE_WHEEL_FILENAME`

## Basemap Tutorials by Sentdex
* basemap_ex01.py: Sentdex's Tutorial Part 1 (see https://www.youtube.com/watch?v=E6gvtfQHJUs)
* basemap_ex02.py: Sentdex's Tutorial Part 2 (see https://www.youtube.com/watch?v=KpS0uEFkfHg)
* basemap_ex03.py: Sentdex's Tutorial Part 3 (see https://www.youtube.com/watch?v=aIX2ZrSWgnc)
* basemap_ex04.py: Sentdex's Tutorial Part 4 (see https://www.youtube.com/watch?v=Xr6sG1QnMbw)
* basemap_ex05.py: Sentdex's Tutorial Part 5 (see https://www.youtube.com/watch?v=kZmYEfTv_WY)
* basemap_ex06.py: Drawing a segment

## References
* Project directory layout: http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/