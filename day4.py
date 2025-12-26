with open("input.txt", "r") as f:
    rows = [x.strip() for x in f.readlines()]


w,h = len(rows[0]), len(rows)

directions = {
        "N":(1,0),
        "NE":(1,1),
        "E":(0,1),
        "SE":(-1,1),
        "S":(-1,0),
        "SW":(-1,-1),
        "W":(0,-1),
        "NW":(1,-1),
        }

# Translate the input to a model
# Moore grid
from dataclasses import dataclass, field
from itertools import chain, zip_longest

@dataclass
class Grid:
    all_cells: dict = field(default_factory=dict)

    def __getitem__(self, target):
        if target in self.all_cells:
            return self.all_cells[target]
        return None

@dataclass
class Cell: 
    pos: tuple
    _grid: Grid = field(repr=False)
    contents: list = field(default_factory=list)

    def add(self, to_add):
        self.contents += [to_add]
        to_add.pos = cell.pos

    def remove(self, to_remove):
        for i,x in enumerate(self.contents):
            if x is to_remove:
                return self.contents.pop(i)
        return None

    def get_nbrs(self):
        nbrs = []
        r,c = self.pos
        for dr,dc in directions.values():
            if r+dr not in range(h): continue
            if c+dc not in range(w): continue
            nbrs += [self._grid[(r+dr, c+dc)]]

        return nbrs

@dataclass
class Roll: 
    cell: Cell = field(repr=True)
    def is_alive(self):
        nbrs = [x.contents[0] for x in self.cell.get_nbrs()]

        roll_nbrs = [x for x in nbrs if type(x) is Roll]

        return len(roll_nbrs) < 4

@dataclass
class Empty: 
    cell: Cell = field(repr=False)


key = {
        "@": Roll,
        ".": Empty,
        }

my_grid = Grid()

for i,row in enumerate(rows):
    for j,col in enumerate(row):
        pos = (i,j)
        cell = Cell(pos, my_grid)
        my_grid.all_cells[pos] = cell
        entity = key[col](cell)
        cell.add(entity)

count = 0
alive = []

flag = False

while not flag: 

    for cell in my_grid.all_cells.values():
        content = [type(x) for x in cell.contents]
        if content[0] is Roll:
            if cell.contents[0].is_alive():
                alive += [cell]
                count += 1

    if not alive:
        flag = True

    for cell in alive:
        cell.contents.pop()
        cell.add(Empty(cell))

    alive = []

    print(count)

