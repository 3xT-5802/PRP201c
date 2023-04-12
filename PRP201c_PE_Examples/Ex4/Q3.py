#Write a program to manage wage of grading assignments
# including name, course, number of assignments, price per assignment, total and tax.
# The program reads data from the file “Database.txt”
# and save to the database file Wage.sqlite using the following table schema.
#   Grade (Nam, Course, NumOfAs, Price, Total, Tax)
#     Where:
#     Total = NumOfAs * Price
#     Tax = 10% of Total if Total >= 2000000, otherwise, Tax =0.
#The program prints the wage of grading Python and sorted in ascending order by NumOfAs.
# The output should be as follows:
#     Wage list:

import sqlite3

conn = sqlite3.connect('Wage.sqlite')
cur = conn.cursor()

init_script = """
    DROP TABLE IF EXISTS Grade;
    
    CREATE TABLE Grade
    (
        Nam TEXT,
        Course TEXT,
        NumOfAs INTEGER,
        Price FLOAT,
        Total FLOAT,
        Tax FLOAT
    );
"""

cur.executescript(init_script)

fhandle = open('Database.txt')

insert_script = """
    INSERT INTO Grade (
        Nam, Course, NumOfAs, Price, Total, Tax
    ) VALUES (?, ?, ?, ?, ?, ?)
"""

def calc(numOfAs, price):
    total = numOfAs * price
    tax = 0
    if total > 2000000:
        tax = 0.1 * total
    return (total, tax)

line_no = 0
for line in fhandle:
    if line_no<2:
        line_no +=1
        continue
    data = line.strip().split()
    if len(data) == 4:
        nam, course, numOfAs, price = data[0], data[1], int(data[2]), float(data[3])
        total, tax = calc(numOfAs, price)
        cur.execute(insert_script, (nam, course, numOfAs, price, total, tax))
        conn.commit()

query = "SELECT * FROM Grade ORDER BY NumOfAs ASC"
cur.execute(query)
data = cur.fetchall()

#format output
def format_output(arr):
    result = ""
    for word in arr:
        result += str(word).ljust(12)
    return result

print("Wage list:")
print(format_output(("Name", "Course", "NumOfAs", "Price", "Total", "Tax")))
for datum in data:
    print(format_output(datum))