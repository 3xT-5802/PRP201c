#Input a number to round decimal places of pi

from math import pi

fraser = str(pi)

length_of_pi = []

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

num = get_int("Enter a positive integer number: ", "The number must be positive.", "The number must be a positive integer.")

for i in range(0, num+2):
    length_of_pi.append(fraser[i])

print("".join(length_of_pi))