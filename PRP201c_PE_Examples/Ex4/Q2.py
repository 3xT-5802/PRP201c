#Given an list of integer numbers in the text file “List.txt”.
# Write a program to read through the file and compute the average of even numbers.
# For example, enter a file name “List.txt” or leave it blank and match the output below.
#Enter file:List.txt

import re

fname = input("Enter a file: ").strip()
if (fname == ''):
    fname = 'List.txt'

fhand = open(fname)

num_lst = list()

count = 0
sum = 0

for line in fhand:
    num_lst = line.strip().split()
    for num in num_lst:
        try:
            n = int(num)
            if (n%2 == 0):
                #count, sum = count + 1 , sum + n
                count += 1
                sum += n
        except:
            continue

print("Avg = ", sum/count if (count>0) else 0)