# This assumes every single splitter is always used
# In the og input that could be an issue

import re

with open('input.txt', 'r') as f:
    inpt = [x.strip('\n') for x in f.readlines()]

#for x in inpt: print(x)

def serialize_inpt(inpt):
    output = []
    for line in inpt:
        output += [[ch for ch in line]]
    return output

def print_tree(tree):
    for line in tree:
        print(''.join(line))

global splits
splits = 0

def navigate_tree(inpt, start_coords):
    s1,s2 = start_coords
    start = inpt[s1][s2]

    if start == 'S':
        inpt[s1+1][s2] = '|'
        return inpt

    assert start == '|'

    n1,n2 = (s1+1,s2)

    next_pos = inpt[n1][n2]
    match next_pos:
        case '.'|'|': 
            inpt[n1][n2] = '|'
        case '^': 
            inpt[n1][n2-1] = '|'
            inpt[n1][n2+1] = '|'
            global splits
            splits += 1
        case _: raise ValueError(next_pos)

    return inpt

a = serialize_inpt(inpt)

i,j = 0,0
while i < len(a)-1:
    if a[i][j] in ('|','S'):
        a = navigate_tree(a, (i,j))
        #print_tree(a)

    if j >= len(a[i])-1:
        i,j = i+1, 0
    else:
        j += 1

print_tree(a)
from collections import Counter
from itertools import chain

print(splits)
print(f"Amt of '^':{Counter(chain(*a))['|']}")

# Need to generate all possible paths from Top to Bottom, only following '|'
# Recursive is most straightforward

# Exit case:
# Laser has reached the end - return coords
# Base case 1/2:
# Laser advances without obstruction - recurse with next coords
# Base case 2/2:
# Laser hits splitter - recurse with left and right next coords respectively

# Input: starting coords
# Output: list of coords from start to end representing that path of the laser

# Looks like the exponential scaling is stronger than my recursion.
# Clearly there has to be a linear formula
# Maybe part 2 has less strict tracing?
# Part 1 test ans was num '^' - 1

import functools


def trace(start, tree):
    @functools.lru_cache
    def recurse(start):
        i,j = start
        count = 0

        if tree[i][j] != '|':
            return 0

        if i >= len(tree)-1:
            return 1

        match tree[i+1][j]:
            case '|':
                count += recurse((i+1,j))

            case '^':
                count += recurse((i+1,j-1))
                count += recurse((i+1,j+1))

        return count

    return recurse(start)

start = (1,70)
trace = trace(start,a)
print(trace)
