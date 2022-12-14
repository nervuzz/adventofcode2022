"""
--- Day 1: Calorie Counting ---
--- Part Two ---
https://adventofcode.com/2022/day/1
"""

curr_elf = alfa_elf = curr_kcal = max_kcal = 0
backpack, totals = [], []

with open("dataset", "r") as fp:
    while True:
        food_kcal = fp.readline()
        if food_kcal == "" or food_kcal.strip() == "":
            curr_elf = curr_elf + 1
            if curr_kcal > max_kcal:
                alfa_elf = curr_elf
                max_kcal = curr_kcal
            totals.append(sum(backpack))
            curr_kcal = 0
            backpack = []
        else:
            backpack.append(int(food_kcal))
            curr_kcal = curr_kcal + int(food_kcal)
        if food_kcal == "":
            break
    top3 = sorted(totals, reverse=True)[:3]
    print(f"TOP3: {top3}")
    print(f"The Elfs in TOP3 carries {sum(top3)} kcal in total!")

# Output:
# TOP3: [66186, 65638, 64980]
# The Elfs in TOP3 carries 196804 kcal in total!
