import math
while True:
    try:
        inp = input().strip().split(" ")
        if len(inp)>2:
            print("Nhap hai so")
            continue
        n = int(inp[0])
        d = int(inp[1])
        if n<1 or n>300000:
            print("Nhap so N trong khoang [1,300000]")
            continue
        if d<1 or d>n:
            print("Nhap so D trong khoang [1,N]")
            continue
        break
    except:
        print("Nhap hai so nguyen duong")

flag = True
while True:
    try:
        inpu = input().strip().split(" ")
        for elem in inpu:
            e = int(elem)
            if e!=0 and e!=1:
                flag = False
                break
        if flag==False:
            print("Nhap day so nguyen duong 0 va 1")
            continue
        break
    except:
        print("Nhap day so nguyen duong 0 va 1")

i = 0
j = 0
y = 0
l = len(inpu)-1
soLan=math.floor(n/d)
while True:
    for x in range(y, y+d+1):
        j+=1
        if int(inpu[x])==0: i+=1
        y+=d
        if y>l: break
    if j==soLan: break

print(i)