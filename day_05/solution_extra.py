"""
--- Day 5: Supply Stacks ---
--- Part Two ---
https://adventofcode.com/2022/day/5
"""


def read_dataset() -> list:
    with open("dataset", "r") as fp:
        yield from [line.rstrip() for line in fp.read().splitlines() if not line.startswith("~")]


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
    _how_much = int(_how_much)
    cargo[_to] = cargo[_from][:_how_much] + cargo[_to]
    del cargo[_from][:_how_much]

msg = "".join(_[0] for _ in cargo.values())

print(f"You've got message: {msg}")

# Output:
# You've got message: DCVTCVPCL
