def compute_gcd(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if ((x%i == 0) and (y%i == 0)):
            gcd = i

    return gcd

def compute_lcm(a, b):
    for i in range(a*b+1):
        if i == 0:
            i += i
            continue
        if i%a != 0 or i%b != 0:
            continue
        return i
        break

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

num_1 = get_int("Enter the first number: ", "Please enter a positive number.", "Please enter a positive number.")
num_2 = get_int("Enter the second number: ", "Please enter a positive number.", "Please enter a positive number.")
if num_1 > 0 and num_2 > 0:
    print("The least common multiple of ", num_1, " and ", num_2, ": ",compute_lcm(num_1, num_2))
    print("The greatest common divisor of ", num_1, " and ", num_2, ": ",compute_gcd(num_1, num_2))