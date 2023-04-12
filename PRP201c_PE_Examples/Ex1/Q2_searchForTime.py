#Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time
# and then splitting the string a second time using a colon.
#  [From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008]
#Count Frequency of all emails , print out the counts.

fhand =open('mbox-short.txt')
d =dict()
for line in fhand:
    if line.startswith('From '):
        line =line.split()
        #print(line)
        line =line[5]
        #print(line)
        line =line[0:2]
        #print(line)
        d[line] =d.get(line,0)+1
        #print(d)

lst =list()
for value,key in d.items():
    lst.append((value,key))
print(lst)