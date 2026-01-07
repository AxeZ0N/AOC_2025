
file = 'input.txt'

boxes = []
with open(file, 'r') as f:
    for line in f.readlines():
        boxes += [tuple(int(x) for x in line.strip().split(','))]
