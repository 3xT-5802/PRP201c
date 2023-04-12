#Compute gcd of 2 positive integer

def compute_gcd(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i

    return gcd

def get_input():
    while True:
        try:
            inp = input("Enter a positive integer number: ")
            num = int(inp)
            if (num<0):
                print("The number must positive!")
                continue
            break
        except:
            print("The number must be a positive integer!")
    return num

a = get_input()
b = get_input()

print("GCD of", a, ", ", b, "is", compute_gcd(a, b))