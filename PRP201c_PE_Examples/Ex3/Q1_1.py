#Input a positive integer and print perfect number

def isPerfectNumber(n):
    sum = 0
    for i in range(1, n):
        if (n%i == 0):
            sum += i
    return sum == n

while True:
    try:
        inp = input("Enter a positive integer number: ")
        num = int(inp)
        if (num<0):
            print("The number must be positive.")
            continue
        break
    except:
        print("The number must be a positive number.")

print("The perfect number from 0 to ", num, ": ")
for i in range(1, num+1):
    if (isPerfectNumber(i)):
        print(i, end = " ")
