import sqlite3

conn = sqlite3.connect('grades.sqlite')
cur = conn.cursor()

init_script = """
    DROP TABLE IF EXISTS Student;

    CREATE TABLE Student(
        Name TEXT,
        term INT,
        grade FLOAT,
        Scholar TEXT
    );
"""
cur.executescript(init_script)

fhandle = open('Data.txt')

line_0 = 0
for line in fhandle:
    if line_0 < 2:
        line_0 += 1
        continue
    data = line.strip().split()
    name = data[0]
    term = int(data[1])
    grade = float(data[2])
    if grade >= 8:
        scholar = 'A'
    elif grade >= 7:
        scholar = 'B'
    else:
        scholar = ''
    cur.execute("""
        INSERT INTO Student(
            Name, term, grade ,Scholar
        ) VALUES (?,?,?,?)""", (name, term, grade, scholar)
    )
    conn.commit()

query = "SELECT * FROM Student ORDER BY grade DESC"
cur.execute(query)
data = cur.fetchall()

#format output
def format_output(arr):
    result = ""
    for word in arr:
        result += str(word).ljust(12)
    return result

print("Scholat list:")
print(format_output(("Name", "term", "grade", "Scholar")))
for datum in data:
    print(format_output(datum))

