"""
--- Day 9: Rope Bridge ---
--- Part Two ---
https://adventofcode.com/2022/day/9
"""
from dataclasses import dataclass


def read_dataset() -> list:
    with open("dataset", "r") as fp:
        yield from [line.strip() for line in fp.read().splitlines()]


@dataclass
class P:
    """A point."""
    x: int
    y: int
    num: str
    moved: bool = False

    @property
    def xy(self) -> str:
        return f"{self.num} {self.x} {self.y}"


def is_touching(h: P, t: P) -> bool:
    if h.xy == t.xy:
        return True  # overlap
    if abs(h.x - t.x) == 1 and abs(h.y - t.y) == 1:
        return True  # diagonally
    if h.x == t.x and abs(h.y - t.y) == 1:
        return True  # same row
    if h.y == t.y and abs(h.x - t.x) == 1:
        return True  # same col
    return False


D = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1),
     "RU": (1, 1), "LU": (-1, 1), "RD": (1, -1), "LD": (-1, -1)}

H = P(0, 0, "H", moved=True)
S = [P(0, 0, "9"), P(0, 0, "8"), P(0, 0, "7"), P(0, 0, "6"), P(0, 0, "5"), P(0, 0, "4"), P(0, 0, "3"), P(0, 0, "2"), P(0, 0, "1")]
out = []
visited = {H.xy}


for step in read_dataset():
    d, v = step.split()

    for _ in range(int(v)):
        H.x += D[d][0]
        H.y += D[d][1]
        visited.add(H.xy)

        if not out:  # First move
            out.append(S.pop())

        h = H
        for T in out:
            if is_touching(h, T):
                h = T
                continue

            if not T.moved:
                T.moved = True
                if S:
                    _ = S.pop()
                    out.append(_)
                    visited.add(_.xy)

            if h.x == T.x or h.y == T.y:
                if h.x == T.x and abs(h.y - T.y) == 2:
                    T.y += 1 if h.y > T.y else -1
                if h.y == T.y and abs(h.x - T.x) == 2:
                    T.x += 1 if h.x > T.x else -1
            else:
                if h.x > T.x:  # diag right
                    dd = "RU" if h.y > T.y else "RD"
                else:  # diag left
                    dd = "LU" if h.y > T.y else "LD"
                T.x += D[dd][0]
                T.y += D[dd][1]
            visited.add(T.xy)
            h = T


print(f"Tail visited {len([i for i in visited if i.startswith('9 ')])} positions")

# Output:
# Tail visited 2386 positions
