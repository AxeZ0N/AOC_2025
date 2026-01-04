# This assumes every single splitter is always used
# In the og input that could be an issue

import re

with open('test_input.txt', 'r') as f:
    inpt = [x.strip('\n') for x in f.readlines()]

#for x in inpt: print(x)

# might be easier to simulate one line at a time?
# heap?
# for each layer
# running queue:
# ...
# ..^ -> +1 split (1)
# .^. -> +2 split (2)
# ^.^ -> +3 split (3)
# ^.. -> +1 split (3)
# ...

# State machine?
# Read 2 bits
# .^.: 2
# ^.^: 3

# Build next line bit by bit?
# S -> |
# .^. -> |.|
# ^.^ -> .|.

# What's needed to generate a new line?
# Previous line, to tell if a laser even hits a splitter
#   How to get prev line: take from tree
# Current line, must handle splitters
#   Hot to get curr line: take from inpt
# Dict of symbol pairs and their evolutions


# This is looking suspiciously like binary addition
# TX:
# Input: line n-1, n
# Returns: tx_line1_line2_line, line n+1
# Algo:
#   Move unobstructed lasers in line n-1 at pos i to line n at pos i
#   Move lasers that hit splitters in line n from line n-1 at pos i to line n at pos i-1, i+1
#   Move all lasers down to row n+1
# Return lines n and n+1


# Algo:
# Start state: empty tree
# tree = lines 0,1 where line 1 == line 0 replace(S,|)
# i = 2
# TX(tree[-1], inpt[i]) -> Next line
# tree.append(Next line)
# i += 2
# repeat

# The simulation worked, but the counting didn't
# Going to try bottom up counting
# Parse two lines at a time?
# Start at len(inpt),0:
# When inpt[i][j] == |, get rid of it, add one to the counter
# Continue until line consumed
# Repeat

from re import findall
from itertools import batched, pairwise


def tx_line1_line2(line1,line2):
    ret = list(line1)
    i = 0
    while i < len(line1):
        ch1,ch2 = line1[i],line2[i]
        match ch1,ch2:
            case '|','^':
                ret[i-1:i+1] = ['|','^','|'] # Replace 3 chars
                ret = ret[:-1] # Delete last char
                i += 1 # Skip next char
            case _:
                ret[i] = ch1
        i += 1

    a = tx_line2_line3(''.join(ret))

    print(''.join(ret), line2)

    return (''.join(ret), a)

def tx_line2_line3(line1):
    ret = list(line1)
    i = 0
    while i < len(line1):
        ch1 = line1[i]
        if ch1 == '|':
            ret[i] = '|'
        else:
            ret[i] = '.'
        i += 1

    return ''.join(ret)

sline = inpt[0].replace('S','|')
tree = [inpt[0],sline]

i = 2
while i < len(inpt):
    a,b = tx_line1_line2(tree[-1],inpt[i])
    input()
    tree += [a,b]
    i += 2

for x in tree: print(x)
print()

a = """
.......S.......
.......|.......
......|^|......
......|.|......
.....|^|^|.....
.....|.|.|.....
....|^|^|^|....
....|.|.|.|....
...|^|^|||^|...
...|.|.|||.|...
..|^|^|||^|^|..
..|.|.|||.|.|..
.|^|||^||.||^|.
.|.|||.||.||.|.
|^|^|^|^|^|||^|
|.|.|.|.|.|||.|
"""

print('a', 'tree')
for i,x in enumerate(zip(a.split(),tree)):
    one, two = x
    print(one,two)

i = len(inpt)-1
splits = 0
while i > 0:
    a = list(tree[i-1])
    b = list(tree[i])
    while len(a):
        ch1,ch2 = a.pop(0), b.pop(0)
        if ch1 == ch2 == '|':
            splits += 1
    print(splits)
    i -= 2

print(splits)
