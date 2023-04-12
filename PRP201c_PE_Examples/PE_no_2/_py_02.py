#Cobination

import re

fname = input("Enter a file name: ")
if fname == '':
    fname = "Text.txt"

fhandle = open(fname)
numLst = list()

for line in fhandle:
    data = line.strip().split(', ')
    for x in range(len(data)):
        for y in range(x, len(data)):
            if x==y: continue
            numLst.append(int(data[x]+data[y]))

print("The original list from the file is: ", data)
print("All numbers combinations: ", numLst)