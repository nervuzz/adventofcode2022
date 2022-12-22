"""
--- Day 3: Rucksack Reorganization ---
https://adventofcode.com/2022/day/3
"""

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.


def read_dataset() -> list:
    with open("dataset", "r") as fp:
        yield from [line.strip() for line in fp.read().splitlines()]


priorities = {chr(lett): prio for prio, lett in enumerate(range(ord("a"), ord("z")+1), start=1)} | {chr(lett): prio for prio, lett in enumerate(range(ord("A"), ord("Z")+1), start=27)}

score = 0
for rucksack in read_dataset():
    size = int(len(rucksack)/2)
    c1, c2 = set(rucksack[:size]), set(rucksack[size:])
    common = (c1 & c2).pop()
    print(f"Common {common} | in {rucksack}")
    score += priorities[common]


print(f"Total: {score}")

# Output:
# Common c | in bZZzJnccqdzcLhrcQDLrDs
# Common w | in FfCfWVfjWTFClClfwjWCfGGwhZSDhSLsSSRpZprLph
# Common t | in mFmTMmFjMMWFfZtttflWjmWTngNHJHggJJHtzgnJvBtBgHdv
# Total: 7811
