"""
--- Day 2: Rock Paper Scissors ---
https://adventofcode.com/2022/day/2
"""

# opponent
# A for Rock, B for Paper, and C for Scissors
# response (me)
# X for Rock, Y for Paper, and Z for Scissors

# (1 for Rock, 2 for Paper, and 3 for Scissors)
# (0 if you lost, 3 if the round was a draw, and 6 if you won)

# A Y -> win for you with a score of 8 (2 because you chose Paper + 6 because you won).
# B X -> loss for you with a score of 1 (1 + 0).
# C Z -> draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).


selection_matrix = {
    "A X": 4,  # D
    "A Y": 8,  # W
    "A Z": 3,  # L
    "B X": 1,  # L
    "B Y": 5,  # D
    "B Z": 9,  # W
    "C X": 7,  # W
    "C Y": 2,  # L
    "C Z": 6,  # D
}

total_score = []

with open("dataset", "r") as fp:
    while True:
        players_selection = fp.readline().strip()
        try:
            score = selection_matrix[players_selection]
            total_score.append(score)
            print(f"Got {players_selection} | score +{score}")
        except KeyError:
            break

print(f"My result is: {sum(total_score)}")

# Output:
# ...
# Got C Y | score +2
# Got B Y | score +5
# My result is: 10994
