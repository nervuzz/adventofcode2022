"""
--- Day 3: Rucksack Reorganization ---
--- Part Two ---
https://adventofcode.com/2022/day/3
"""


def read_dataset() -> list:
    with open("dataset", "r") as fp:
        yield from [line.strip() for line in fp.read().splitlines()]


priorities = {chr(lett): prio for prio, lett in enumerate(range(ord("a"), ord("z")+1), start=1)} | {chr(lett): prio for prio, lett in enumerate(range(ord("A"), ord("Z")+1), start=27)}

score = 0
group = []
for rucksack in read_dataset():
    group.append(rucksack)
    if len(group) == 3:
        common = set(group[0]) & set(group[1]) & set(group[2])
        print(f"Common item is {common}")
        score += priorities[common.pop()]
        group.clear()


print(f"Total: {score}")

# Output:
# Common item is {'N'}
# Common item is {'V'}
# Common item is {'Z'}
# Total: 2639
