"""
--- Day 8: Treetop Tree House ---
https://adventofcode.com/2022/day/8
"""
from dataclasses import dataclass


def read_dataset() -> list:
    with open("dataset", "r") as fp:
        yield from [line.strip() for line in fp.read().splitlines()]


@dataclass
class Tree:
    """A tree."""
    x: int
    y: int
    h: int
    id: str = None

    def __post_init__(self):
        self.id = f"{self.x}|{self.y}"


forest = []

for y, yt in enumerate(read_dataset()):
    row = []
    for x, xt in enumerate(yt):
        row.append(Tree(x, y, int(xt)))
    forest.append(row)


visible = set()

# L->R
for r in forest:
    maxh = r[0].h
    for t in r:
        if t.x == 0 or t.y == 0:
            visible.add(t.id)
            continue
        if t.h > maxh:
            maxh = t.h
            visible.add(t.id)
# T->B
for i in range(0, len(forest[0])):
    maxh = forest[0][i].h
    for r in forest:
        if r[i].x == 0 or r[i].y == 0:
            visible.add(r[i].id)
            continue
        if r[i].h > maxh:
            maxh = r[i].h
            visible.add(r[i].id)

# R->L
for r in forest:
    maxh = r[-1].h
    for t in r[::-1]:
        if t.x == len(forest)-1 or t.y == len(forest)-1:
            visible.add(t.id)
            continue
        if t.h > maxh:
            maxh = t.h
            visible.add(t.id)

# B->T
for i in range(len(forest[0])-1, 0, -1):
    maxh = forest[-1][i].h
    for r in forest[::-1]:
        if r[i].x == len(forest)-1 or r[i].y == len(forest)-1:
            visible.add(r[i].id)
            continue
        if r[i].h > maxh:
            maxh = r[i].h
            visible.add(r[i].id)


print(f"{len(visible)} trees are visible from outside the grid")

# Output:
# 1604 too low
# 1690 trees are visible from outside the grid
