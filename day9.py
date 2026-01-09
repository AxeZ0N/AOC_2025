
# Input is list of x,y coords.
# Find largest rectangle possible using coords as diagonal corners

# Might need to sort by x and y coords separately
# Start with (sorted) tiles[0] and tiles[-1]

# Part 2, input forms an n-gon, largest possible rectangle within n-gon
# Going to write a visualizer first.
# Ok, not super useful, too big. Crashed my chromebook
# Need a polygon collision/contains algorithm
# Raycast points on the same x or same y, if any boundaries crossed: fail

from itertools import pairwise, combinations
import numpy
import shapely
from shapely import plotting
from shapely import Polygon
from matplotlib import pyplot as plt

file = 'input.txt'
x,y = numpy.loadtxt(file,delimiter=',',unpack=True)

tiles = [(int(c),int(r)) for c,r in zip(x,y)]

p = Polygon(tiles)

max_p1, max_p2 = 0,0


for c1,c2 in combinations(tiles,2):
    x1,y1 = c1
    x2,y2 = c2
    x_min,x_max = min(x1,x2), max(x1,x2)
    y_min,y_max = min(y1,y2), max(y1,y2)

    box = shapely.box(x_min,y_min,x_max,y_max)

    area = (x_max-x_min + 1) * (y_max-y_min+1)
    if p.contains(box):
        max_p2 = max(area, max_p2)

    max_p1 = max(area, max_p1)


print(max_p1, max_p2)

