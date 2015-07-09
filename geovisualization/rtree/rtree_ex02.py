from rtree import index
from shapely.geometry import LineString

import numpy as np

def main():
    coords_list = [
        [[1., 1.], [1., 1.5]],
        [[2., 2.5], [1., 3.5]],
        [[3., 5.], [4., 2.]],
        [[2.5, 5.], [2., 3.]]
    ]

    linestrings = [LineString(coords) for coords in coords_list]
    idx = index.Index()  # r-tree index

    for i, linestring in enumerate(linestrings):
        idx.insert(i, linestring.bounds, linestring)

    # Create a bounding box by expanding the first linestring's bounding box
    # Then count the number of items that are in that bounding box, and
    # find the k-nearest neighbors (actually k - 1 because idx.nearest() returns
    # the index of the first linestring too.
    bbox = np.array(linestrings[0].bounds) + np.array([-1., -1., 1., 1.])  # Expand the bounding box a bit
    num = idx.count(bbox) # Count the number of items that are in this bounding box
    print "Number of items in a given bbox, and their indices:", num, list(idx.nearest(linestrings[0].bounds, num))
    print

    print "Get the raw objects (line strings):"
    objects = idx.nearest(linestrings[0].bounds, num, objects='raw')
    for obj in objects:
        print obj
    print

    # Delete an index
    print "Delete an index"
    idx.delete(1, bbox)
    print idx.count(bbox)
    print "... I'm confused because the item is not deleted..."
    print
    print "Ok, the bounding box must match the shape of the object... (http://lists.gispython.org/pipermail/community/2009-November/002379.html"
    idx.delete(1, linestrings[1].bounds)
    print idx.count(bbox)

if __name__ == "__main__":
    main()