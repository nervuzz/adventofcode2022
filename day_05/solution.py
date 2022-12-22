"""
--- Day 5: Supply Stacks ---
https://adventofcode.com/2022/day/5
"""


def read_dataset() -> list:
    with open("dataset", "r") as fp:
        yield from [line.rstrip() for line in fp.read().splitlines() if not line.startswith("~")]


# ~[N]         [C]     [Z]
# ~[Q] [G]     [V]     [S]         [V]
# ~[L] [C]     [M]     [T]     [W] [L]
# ~[S] [H]     [L]     [C] [D] [H] [S]
# ~[C] [V] [F] [D]     [D] [B] [Q] [F]
# ~[Z] [T] [Z] [T] [C] [J] [G] [S] [Q]
# ~[P] [P] [C] [W] [W] [F] [W] [J] [C]
# ~[T] [L] [D] [G] [P] [P] [V] [N] [R]
# ~ 1   2   3   4   5   6   7   8   9
# ~

S1 = ["N", "Q", "L", "S", "C", "Z", "P", "T", ]
S2 = ["G", "C", "H", "V", "T", "P", "L", ]
S3 = ["F", "Z", "C", "D", ]
S4 = ["C", "V", "M", "L", "D", "T", "W", "G", ]
S5 = ["C", "W", "P", ]
S6 = ["Z", "S", "T", "C", "D", "J", "F", "P", ]
S7 = ["D", "B", "G", "W", "V", ]
S8 = ["W", "H", "Q", "S", "J", "N", ]
S9 = ["V", "L", "S", "F", "Q", "C", "R", ]

cargo = {
    "1": S1, "2": S2, "3": S3, "4": S4, "5": S5, "6": S6, "7": S7, "8": S8, "9": S9,
}

# move 6 from 2 to 1

for move in read_dataset():
    _, _how_much, _, _from, _, _to = move.split()
    for i in range(int(_how_much)):
        cargo[_to].insert(0, cargo[_from].pop(0))

msg = "".join([x.pop(0) for x in cargo.values()])

print(f"You've got message: {msg}")

# Output:
# You've got message: SVFDLGLWV
