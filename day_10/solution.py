"""
--- Day 10: Cathode-Ray Tube ---
https://adventofcode.com/2022/day/10
"""


def read_dataset() -> list:
    with open("dataset", "r") as fp:
        yield from [line.strip() for line in fp.read().splitlines()]

# 20th, 60th, 100th, 140th, 180th, and 220th cycles
# noop 1c addx 2c


X = 1
A = []
R = []

for ins in read_dataset():
    if ins.startswith("noop"):
        R.extend([X])
    else:
        R.extend([X, X])
        X += int(ins.split()[-1])

R = 20*R[20-1]+60*R[60-1]+100*R[100-1]+140*R[140-1]+180*R[180-1]+220*R[220-1]

print(f"Sum of these six signal strengths is {R}")

# Output:
# 336 too low
# Sum of these six signal strengths is 17020
