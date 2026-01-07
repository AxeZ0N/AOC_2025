# 3D space shortest pairs problem
from math import sqrt

file = 'input.txt'

boxes = []
with open(file, 'r') as f:
    for line in f.readlines():
        boxes += [tuple(int(x) for x in line.strip().split(','))]

def get_dist_sqrd(c1,c2):
    a,b,c = c1
    d,e,f = c2

    return (a-d)**2 + (b-e)**2 + (c-f)**2

#print(boxes)

def build_dist_index(boxes):
    box_pairs = []

    inner_list = boxes.copy()

    for c1 in boxes:
        for c2 in inner_list:
            if c1 == c2: continue
            box_pairs += [(get_dist_sqrd(c1,c2), (c1,c2))]

        inner_list.pop(0)

    box_pairs.sort()

    return box_pairs

box_pairs = build_dist_index(boxes)
circuits = [[x] for x in boxes.copy()]

# Must build circuits out of sequential closest pairs
# First, need index of distances
# Second, need a way of tracking existing circuits

# I didn't account for groups having to merge eventually
# All circuits start out alone
# Loop:
#   c1, c2
#   match (c1,c2 in group)
#       case both:
#           remove both old groups from list
#           combine
#           add to list
#       case one:
#           add other to group
#       case none:
#           new group
#           add to list
#
#   for coord in coords_list:
#       grps[coord] = len(coord.grp)

max_ = 10 if 'test' in file else 1000
i = 0

b1 = (216,146,977)
b2 = (117,168,530)
j = 0
for d,pair in box_pairs:
    if b1 in pair and b2 in pair:
        print(pair, j)
    j += 1

while len(circuits) > 1:
#max_ = 29
#while i < max_:

    dist, pair = box_pairs.pop(0)
    if i % 100 == 0:
        print(f"Pair: {pair}, i: {i}, circuits: {len(circuits)}")
    box1, box2 = pair

    box1_group = [grp for grp in circuits if box1 in grp][0]
    box2_group = [grp for grp in circuits if box2 in grp][0]

    if box1_group is box2_group:
        pass

    elif len(box1_group) == 1 and len(box2_group) == 1:
        circuits = [grp for grp in circuits if box1 not in grp]
        circuits = [grp for grp in circuits if box2 not in grp]
        circuits += [[box1,box2]]

    elif len(box1_group) > 1:
        circuits = [grp for grp in circuits if box2 not in grp]
        for grp in circuits:
            if box1 in grp: grp += [x for x in box2_group]

    elif len(box2_group) > 1:
        circuits = [grp for grp in circuits if box1 not in grp]
        for grp in circuits:
            if box2 in grp: grp += [x for x in box1_group]

    else:
        raise ValueError(dist,pair)

    #print(circuits)
    #print(sorted([len(x) for x in circuits],reverse=True))
    #input()
    #print('done')

    i += 1

abc = sorted([len(x) for x in circuits],reverse=True)
print(box1,box2)
print(box1[0]*box2[0])
#print(abc[0]*abc[1]*abc[2])
