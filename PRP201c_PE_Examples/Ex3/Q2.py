#Write a program that prompts for a file name, then opens that file and
# reads through the file DNSList.txt, looking for lines Of the form:
#Location: France
#Count the number of DSN server from each country.
# Once you have accumulated the counts for each name, print out the counts, sorted by name.
#For example, enter a file name "DNSList.txt" or leave it blank and match the output below.
#Enter file:DNSList.txt
#DNS server list:
#Country            Count
#Brazil             1
#France             6
#India              1
#United             5
import operator
import re
fname = input("Enter file: ")
if (fname == ''):
    fname = 'DNSList.txt'
fhand = open(fname)

DNS_server = dict()

for line in fhand:
    line = line.strip()
    # Take the line start with 'Location'
    if (not line.startswith('Location')): continue
    # This regex will Ignore the line start with 'Location' which not having (Country) after Location:
    lst = line.split()
    DNS_server[lst[1]] = DNS_server.get(lst[1], 0) + 1

sorted_DNS_server_asc_key = dict(sorted(DNS_server.items(), key=operator.itemgetter(0)))
sorted_DNS_server_dec_key = dict(sorted(DNS_server.items(), key=operator.itemgetter(0), reverse=True))
sorted_DNS_server_asc_value = dict(sorted(DNS_server.items(), key=operator.itemgetter(1)))
sorted_DNS_server_dec_value = dict(sorted(DNS_server.items(), key=operator.itemgetter(1), reverse=True))

print("DNS server list:")
print("Country  \tCount")
for k,v in sorted_DNS_server_asc_key.items():
    print(k, '  \t', v)