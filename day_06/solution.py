"""
--- Day 6: Tuning Trouble ---
https://adventofcode.com/2022/day/6
"""


def read_dataset() -> list:
    with open("dataset", "r") as fp:
        yield from [line.strip() for line in fp.read().splitlines()]


def subroutine(signal_buffer: str | list) -> int:
    unique = []
    for idx, char in enumerate(signal_buffer, start=1):
        if char not in unique:
            unique.append(char)
            print(f"{idx} new unique {char}")

            if len(unique) == 4:
                print(f"Magic packet found at {idx}: {unique}")
                return idx
        else:
            print(f"Char not unique: {char}, doing clean-up")
            del unique[:unique.index(char) + 1]
            unique.append(char)


for buffer in read_dataset():
    subroutine(buffer)

# Output:
# Char not unique: s, doing clean-up
# 1621 new unique z
# 1622 new unique m
# 1623 new unique p
# Magic packet found at 1623: ['s', 'z', 'm', 'p']
