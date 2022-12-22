"""
--- Day 4: Camp Cleanup ---
--- Part Two ---
https://adventofcode.com/2022/day/3
"""


def read_dataset() -> list:
    with open("dataset", "r") as fp:
        yield from [line.strip() for line in fp.read().splitlines()]


pairs_count = 0

for pair in read_dataset():
    elf_1, elf_2 = pair.split(",")
    elf_1_start, elf_1_stop = elf_1.split("-")
    elf_2_start, elf_2_stop = elf_2.split("-")

    elf_1_set = set(range(int(elf_1_start), int(elf_1_stop)+1))
    elf_2_set = set(range(int(elf_2_start), int(elf_2_stop)+1))

    if len(list(elf_1_set & elf_2_set)) > 0:
        pairs_count += 1


print(f"Found {pairs_count} pairs")

# Output:
# Found 905 pairs
