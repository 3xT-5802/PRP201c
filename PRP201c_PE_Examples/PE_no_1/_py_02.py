import re

fname = input("Enter a file name: ")
if fname == '':
    fname = "Text.txt"

fhandle = open(fname)
numLst = list()

for line in fhandle:
    data = line.strip().split(', ')
    for datum in data:
        if int(datum) < 0: continue
        numLst.append(datum)

print("The original list is: ", data)
print("List after removing negative numbers: ", numLst)