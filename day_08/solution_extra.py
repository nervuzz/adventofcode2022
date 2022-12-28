"""
--- Day 8: Treetop Tree House ---
--- Part Two ---
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


def traverse(x, y, h, arr) -> int:
    L = []
    for t in arr[y][:x][::-1]:
        L.append(t.h)
        if t.h >= h:
            break

    R = []
    for t in arr[y][x+1:]:
        R.append(t.h)
        if t.h >= h:
            break

    T = []
    for i in range(y - 1, -1, -1):
        T.append(arr[i][x].h)
        if arr[i][x].h >= h:
            break

    B = []
    for i in range(y+1, len(arr)):
        B.append(arr[i][x].h)
        if arr[i][x].h >= h:
            break

    return len(L) * len(R) * len(T) * len(B)


scenic_score = []

for r in forest:
    for t in r:
        scenic_score.append(
            traverse(t.x, t.y, t.h, forest)
        )

# print(sorted(scenic_score))
print(f"Max scenic score is {max(scenic_score)}")

# Output:
# 59488 too low
# Max scenic score is 535680
