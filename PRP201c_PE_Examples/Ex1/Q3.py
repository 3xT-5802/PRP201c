#Write a program to read through the MovieList.txt
# and add info to database named dbmovieList.sqlite.
# If movieID start with 'Act' then des is 'Action Movie' else des is 'Sciendtific movie'.
# '''create table MovieList(
#        movieID TEXT,
#        length INTEGER,
#        Des TEXT
#    );'''
#Print out top 3  item in database sort by length descending

import sqlite3
import re

conn = sqlite3.connect('dbmovieList.sqlite')
cur = conn.cursor()

cur.executescript('''
    drop table if exists MovieList;

    create table MovieList(
        movieID TEXT,
        length INTEGER,
        Des TEXT
    );
''')

fname = 'MovieList.txt'
fhand = open(fname, 'r')

for line in fhand:
    line = line.strip()
    lst = re.split('[\s]+', line)

    if (len(lst) < 2): continue
    movie_id = lst[0]

    try:
        length = int(lst[1])
    except:
        continue

    des = ''
    if (movie_id.lower().startswith('act')):
        des = 'Action Movie'
    else:
        des = 'Scientific movie'
    # print(movie_id,length,des)

    cur.execute('''
        insert into MovieList(movieID,length,Des) values (?,?,?)        
    ''', (movie_id, length, des))

    conn.commit()
sqlstr = 'select movieID,length,Des from MovieList order by length desc limit 3'

for entry in cur.execute(sqlstr):
    print(entry[0], entry[1], entry[2])

cur.close()