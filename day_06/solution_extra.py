"""
--- Day 6: Tuning Trouble ---
--- Part Two ---
https://adventofcode.com/2022/day/6
"""


def read_dataset() -> list:
    with open("dataset", "r") as fp:
        yield from [line.strip() for line in fp.read().splitlines()]


def subroutine(signal_buffer: str) -> int:
    unique = []
    for idx, char in enumerate(signal_buffer, start=1):
        if char not in unique:
            unique.append(char)
            print(f"{idx} new unique {char}")

            if len(unique) == 14:
                print(f"Message-start packet found at {idx}: {unique}")
                return idx
        else:
            print(f"Char not unique: {char}, doing clean-up")
            del unique[:unique.index(char) + 1]
            unique.append(char)


for buffer in read_dataset():
    subroutine(buffer)

# Output:Char not unique: b, doing clean-up
# 3771 new unique j
# 3772 new unique r
# 3773 new unique s
# 3774 new unique h
# Message-start packet found at 3774: ['t', 'f', 'm', 'z', 'd', 'w', 'n', 'p', 'v', 'b', 'j', 'r', 's', 'h']
