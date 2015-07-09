"""
This is a tutorial from the following web page: http://toblerity.org/rtree/tutorial.html
"""
from rtree import index

def main():
    idx = index.Index()
    left, bottom, right, top = (0.0, 0.0, 1.0, 1.0)
    idx.insert(0, (left, bottom, right, top))

    # Intersection
    print list(idx.intersection((1.0, 1.0, 2.0, 2.0)))
    print list(idx.intersection((1.0000001, 1.0000001, 2.0, 2.0)))

    # Nearest neighbors
    idx.insert(1, (left, bottom, right, top))
    list(idx.nearest((1.0000001, 1.0000001, 2.0, 2.0), 1))

if __name__ == "__main__":
    main()