"""
--- Day 1: Calorie Counting ---
https://adventofcode.com/2022/day/1
"""

curr_elf = alfa_elf = curr_kcal = max_kcal = 0
curr_elf_arr = []

with open("dataset", "r") as fp:
    while True:
        food_kcal = fp.readline()
        if food_kcal == "" or food_kcal.strip() == "":
            curr_elf = curr_elf + 1
            if curr_kcal > max_kcal:
                print(f"New max found: {curr_kcal}, Elf {curr_elf} carries {curr_elf_arr}")
                alfa_elf = curr_elf
                max_kcal = curr_kcal
            curr_kcal = 0
            curr_elf_arr = []
        else:
            curr_elf_arr.append(int(food_kcal))
            curr_kcal = curr_kcal + int(food_kcal)
        if food_kcal == "":
            break
    print(f"Ask Elf no. {alfa_elf} if you need food coz he carries {max_kcal} kcal in total!")

# Output:
# New max found: 26916, Elf 1 carries [11334, 6264, 9318]
# New max found: 47650, Elf 2 carries [1209, 4404, 3988, 5816, 3890, 4990, 2796, 4199, 5439, 4249, 2938, 1120, 2612]
# New max found: 50864, Elf 4 carries [5499, 3383, 3991, 6695, 2008, 2478, 5240, 4782, 6979, 4205, 5604]
# New max found: 54721, Elf 10 carries [22304, 32417]
# New max found: 62783, Elf 17 carries [7389, 8219, 9570, 9070, 1506, 9126, 6811, 8924, 2168]
# New max found: 66186, Elf 35 carries [3949, 4571, 5785, 5968, 2506, 4511, 5234, 6501, 5448, 4961, 2762, 3742, 6426, 3822]
# Ask Elf no. 35 if you need food coz he carries 66186 kcal in total!
