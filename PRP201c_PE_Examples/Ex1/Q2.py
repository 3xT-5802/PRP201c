#Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time
# and then splitting the string a second time using a colon.
#  [From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008]
#Count Frequency of all emails , print out the counts.

import re

fhand = open('mbox-short.txt')

EmailFrequency = dict()

for line in fhand:
    line = line.strip()
    # Take the line start with 'From'
    if(not line.startswith('From')): continue
    #This regex will Ignore the line start with 'From' which not having (Time) after Email
    lst = re.findall(' (.+@.+?) ',line)
    if(len(lst)>0):
        EmailFrequency[lst[0]] = EmailFrequency.get(lst[0],0) + 1

for k,v in EmailFrequency.items():
    print(k, ':', v)

