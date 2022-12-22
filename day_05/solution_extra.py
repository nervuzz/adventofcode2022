"""
--- Day 5: Supply Stacks ---
--- Part Two ---
https://adventofcode.com/2022/day/5
"""


def read_dataset() -> list:
    with open("dataset", "r") as fp:
        yield from [line.strip() for line in fp.read().splitlines()]


...

# Output:

