"""
--- Day 9: Rope Bridge ---
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

    @property
    def xy(self) -> str:
        return f"{self.x} {self.y}"


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

H = P(0, 0)
T = P(0, 0)

visited = {H.xy}

for step in read_dataset():
    d, v = step.split()

    for _ in range(int(v)):
        H.x += D[d][0]
        H.y += D[d][1]
        # visited.add(H.xy)

        if is_touching(H, T):
            continue
        elif H.x == T.x or H.y == T.y:
            if H.x == T.x and abs(H.y - T.y) == 2:
                T.y += 1 if H.y > T.y else -1
            if H.y == T.y and abs(H.x - T.x) == 2:
                T.x += 1 if H.x > T.x else -1
        else:
            if H.x > T.x:  # diag right
                dd = "RU" if H.y > T.y else "RD"
            else:  # diag left
                dd = "LU" if H.y > T.y else "LD"
            T.x += D[dd][0]
            T.y += D[dd][1]
        visited.add(T.xy)

# print(f"Visited: {visited}")
print(f"Visited len {len(visited)}")

# Output:
# Visited len 6181
