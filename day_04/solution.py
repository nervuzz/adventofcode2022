"""
--- Day 4: Camp Cleanup ---
https://adventofcode.com/2022/day/4
"""


def read_dataset() -> list:
    with open("dataset", "r") as fp:
        yield from [line.strip() for line in fp.read().splitlines()]


pairs_count = 0

for pair in read_dataset():
    elf_1, elf_2 = pair.split(",")
    elf_1_start, elf_1_stop = elf_1.split("-")
    elf_2_start, elf_2_stop = elf_2.split("-")

    if int(elf_1_start) >= int(elf_2_start) and int(elf_1_stop) <= int(elf_2_stop):
        print(f"{pair} | Elf 1 covers Elf 2")
        pairs_count += 1
        continue

    if int(elf_2_start) >= int(elf_1_start) and int(elf_2_stop) <= int(elf_1_stop):
        print(f"{pair} | Elf 2 covers Elf 1")
        pairs_count += 1

print(f"Found {pairs_count} pairs")

# Output:
# 77-92,77-94 | Elf 1 covers Elf 2
# 37-99,67-90 | Elf 2 covers Elf 1
# 43-43,34-43 | Elf 1 covers Elf 2
# Found 576 pairs
