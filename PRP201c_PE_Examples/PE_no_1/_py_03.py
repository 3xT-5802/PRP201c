import sqlite3

conn = sqlite3.connect("EMPLIST.sqlite")
cur = conn.cursor()

init_script = """
    DROP TABLE IF EXISTS DEPT;
    
    DROP TABLE IF EXISTS EMP;
    
    CREATE TABLE DEPT(
        DeptID TEXT,
        DName TEXT
    );
    
    CREATE TABLE EMP(
        ID TEXT,
        Name TEXT,
        DeptID TEXT
    );
"""

cur.executescript(init_script)

fhandle = open("Dept.txt")
fhand = open("Data.txt")

line_no_Dept = 0
line_no_Emp = 0

for line_Dept in fhandle:
    if line_Dept == "": break
    if line_no_Dept < 1:
        line_no_Dept += 1
        continue
    data_Dept = line_Dept.strip()
    DeptID = data_Dept[0:2]
    DName = data_Dept[2:].strip()
    cur.execute("""
            INSERT INTO DEPT(
                DeptID, DName
            )VALUES (?,?)""", (DeptID, DName)
                )
    conn.commit()

for line_Emp in fhand:
    if line_no_Emp < 1:
        line_no_Emp += 1
        continue
    data_Emp = line_Emp.strip().split("\t")
    EmpID = data_Emp[0]
    EmpName = data_Emp[1]
    DID = data_Emp[2]

    cur.execute("""
        INSERT INTO EMP(
            ID, Name, DeptID
        )VALUES (?,?,?)""", (EmpID, EmpName, DID)
    )
    conn.commit()

cur.execute("""SELECT emp.ID, emp.Name, dept.DName FROM EMP emp, DEPT dept WHERE emp.DeptID = dept.DeptID ORDER BY emp.Name ASC""")
data = cur.fetchall()

def format_output(arr):
    result = ""
    for word in arr:
        result += str(word).ljust(20)
    return result

print("Employee list:")
print(format_output(("ID", "Full Name", "Dept Name")))
for datum in data:
    print(format_output(datum))

