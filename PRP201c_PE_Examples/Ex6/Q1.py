#Write a program that repeatedly prompts a user for numbers
# until the user enters a positive integer number.
# Once a valid number is entered, the program converts the number into a binary number
# and print out the result.
# If the user enters anything other than a valid number catch it with a try/except
# and put out an appropriate message and ignore the number.
# For example, enter -I and 10 and match the output below.
#Enter a positive integer number: -1
#The number must be positive.
#Enter a positive integer number: 12
#12 is converted into binary: 1100

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
bin_num = bin(num).replace("0b", "")
print(num, "is converted to binary: ", bin_num)
