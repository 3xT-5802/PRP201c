#Compute gcd of 2 positive integer

def compute_gcd(a, b):
    if b == 0:
        return a
    if (b>a):
        (a, b) = (b, a)
    return compute_gcd(b, a - b)

def get_input():
    while True:
        try:
            inp = input("Enter a positive integer number: ")
            num = int(inp)
            if (num<=0):
                print("The number must positive!")
                continue
            break
        except:
            print("The number must be a positive integer!")
    return num

a = get_input()
b = get_input()

print("GCD of", a, ", ", b, "is", compute_gcd(a, b))