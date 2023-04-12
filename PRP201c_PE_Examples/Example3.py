import math

def isPrime(n):
		if (n<2): return 0
		for i in range(2,math.floor(math.sqrt(n)+1)):
			if n%i==0: return False
		return True

def isFibonacci(n):
	t1 = 1
	t2 = 1
	if(n==1): return 1
	while(t2<n):
		t = t2
		t2 = t1 + t2
		t1 = t
	return n==t2

def fiboEle(n):
	x=1
	y=1
	for i in range(3,n+1):
		z=y
		y+=x
		x=z
	return y

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
print(isFibonacci(a), isPrime(a), fiboEle(a))