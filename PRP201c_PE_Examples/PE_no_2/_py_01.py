#Rolling 2 dice

import random

def get_int(msg, ermsg1, ermsg2):
    while True:
        try:
            inp = input(msg)
            num = int(inp)
            if num <= 0:
                print(ermsg1)
                continue
            break
        except:
            print(ermsg2)
    return num

while True:
    inp = get_int("Enter an integer number of total: ", "Please enter a positive number.", "Please enter a positive number.")
    if inp<2 and inp>12:
        print("Please enter a positive number in range [2, 12].")
        continue
    break

i = 0

print("Dice Thrower")
print("==============")

while True:
    dice1_no = random.randint(1, 6)
    dice2_no = random.randint(1, 6)
    i += 1
    print("Result of throw: ", i, dice1_no, " + ", dice2_no)
    if (dice1_no+dice2_no) == inp:
        print("You got your total in ", i, "throws")
        break