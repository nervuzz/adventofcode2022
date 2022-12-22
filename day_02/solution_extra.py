"""
--- Day 2: Rock Paper Scissors ---
--- Part Two ---
https://adventofcode.com/2022/day/2
"""
from enum import IntEnum

# (1 for Rock, 2 for Paper, and 3 for Scissors)
# X means you need to lose
# Y means you need to end the round in a draw
# Z means you need to win


total_score = []


ShapePoints = {
    "A": 1,
    "B": 2,
    "C": 3,
}

OutcomePoints = {
    "X": 6,
    "Y": 3,
    "Z": 0,
}


def my_score(their_choice: str) -> int:
    shape, outcome = their_choice.split()
    rival_points = ShapePoints[shape] + OutcomePoints[outcome]
    if outcome == "Y":
        my_points = rival_points
    elif outcome == "X":
        if shape == "A":
            my_points = 3
        elif shape == "B":
            my_points = 1
        else:
            my_points = 2
    else:
        if shape == "A":
            my_points = 2 + 6
        elif shape == "B":
            my_points = 3 + 6
        else:
            my_points = 1 + 6
    print(f"Shape: {shape} | Outcome: {outcome} | Rival: {rival_points} | My: {my_points}")
    return my_points


with open("dataset", "r") as fp:
    while True:
        players_selection = fp.readline().strip()
        try:
            score = my_score(players_selection)
            total_score.append(score)
        except (KeyError, ValueError):
            break

print(f"My result is: {sum(total_score)}")

# Output:
# ...
# Shape: C | Outcome: Y | Rival: 6 | My: 6
# Shape: B | Outcome: Y | Rival: 5 | My: 5
# My result is: 12526
