
# Input is list of x,y coords.
# Find largest rectangle possible using coords as diagonal corners

# Might need to sort by x and y coords separately
# Start with (sorted) tiles[0] and tiles[-1]

# Part 2, input forms an n-gon, largest possible rectangle within n-gon
# Going to write a visualizer first.
# Ok, not super useful, too big. Crashed my chromebook

from itertools import pairwise

file = 'input.txt'
tiles = []
with open(file, 'r') as f:
    for line in f.readlines():
        tiles += [tuple(int(x) for x in line.strip().split(','))]

#tiles.sort()

def draw_line(p1,p2,graph):
    c1,r1 = p1
    c2,r2 = p2

    draw_row = c1 == c2
    draw_col = r1 == r2
    
    if draw_row and not draw_col:
        dir_ = 'row'
        direction = -1 if r1 > r2 else 1
    elif draw_col and not draw_row:
        dir_ = 'col'
        direction = -1 if c1 > c2 else 1

    print(f"Plane: {dir_}, direction: {direction}")
    while (c1,r1) != p2:
        print(c1,r1,p2)
        graph[r1][c1] = 'X'
        if dir_ == 'row':
            r1 += direction
        elif dir_ == 'col':
            c1 += direction

    return graph

def find_area(corner1,corner2):
    # Find area of rectangle from two diagonal corners
    (r1,c1),(r2,c2 ) = corner1,corner2

    side1 = abs(r2-r1)+1
    side2 = abs(c2-c1)+1

    return side1 * side2

areas = []
inner_tiles = tiles.copy()

for t1 in tiles:
    for t2 in inner_tiles:
        if t1 == t2: continue
        areas += [(find_area(t1,t2), (t1,t2))]
    inner_tiles.pop(0)

areas.sort()

print(areas[-1])
