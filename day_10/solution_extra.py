"""
--- Day 10: Cathode-Ray Tube ---
--- Part Two ---
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

line = []
px = 0
for x in R:
    if px in [x-1, x, x+1]:
        line.append("#")
    else:
        line.append(".")

    px += 1
    if px % 40 == 0 and px > 0:
        print(f"{''.join(line)}")
        line = []
        i = 0


# Output:
# RLEZFLGE
#
#  ###..#....####.####.####.#.....##..####.
#  #..#.#....#.......#.#....#....#..#.#....
#  #..#.#....###....#..###..#....#....###..
#  ###..#....#.....#...#....#....#.##.#....
#  #.#..#....#....#....#....#....#..#.#....
#  #..#.####.####.####.#....####..###.####.
