while True:
    for x in range(l-d, l+1):
        j+=1
        if int(inpu[x])==0: i+=1
        if l<d: break
        l=l-d
        if l<0: break
    if j==soLan: break

print(i)