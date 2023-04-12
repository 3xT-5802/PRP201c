import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('DNSList.sqlite')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Creating table as per requirement
sql = '''
   DROP TABLE IF EXISTS DNS;

   CREATE TABLE DNS(
   IP TEXT NOT NULL,
   Reliability INTEGER,
   Description TEXT
);'''
cursor.executescript(sql)

# read data from the text file
with open('DNSList.txt') as f:
    lines = f.readlines()

insert_query = "INSERT INTO DNS VALUES(?, ?, ?)"
# add data to db
for line in lines:
    if (not line.startswith('IP Address')): continue
    data = line.strip().split(": ")
    if int(data[2]) < 50:
        cursor.execute(insert_query, (data[1], data[2], "Low"))
    else:
        cursor.execute(insert_query, (data[1], data[2], "Normal"))
    conn.commit()

# display the data in table format
cursor.execute("SELECT * FROM DNS ORDER BY Reliability DESC;")
dns_servers = cursor.fetchall()
print("DNS server list: ")
print("   \tIP       \t\t\tReliability       Description")
for row in dns_servers:
    print(row[0], row[1], row[2], sep='            \t')