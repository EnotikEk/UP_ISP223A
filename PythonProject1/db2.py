import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS students')

cursor.execute('''
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    group_name TEXT NOT NULL,
    teacher TEXT NOT NULL,
    attendance TEXT DEFAULT '' CHECK(attendance IN ('', 'н', 'у', 'б'))
)
''')

students = [
    ('Белавин Лев', 'ИСП-223а', 'Светлана Георгиевна', ''),
    ('Брунцев Михаил', 'ИСП-223а', 'Светлана Георгиевна', ''),
    ('Зайцев Андрей', 'ИСП-223а', 'Светлана Георгиевна', ''),
    ('Иванова Жанна', 'ИСП-223а', 'Светлана Георгиевна', ''),
    ('Ковалевич София', 'ИСП-223а', 'Светлана Георгиевна', ''),
    ('Андрей', 'ИСП-223п', 'Светлана Георгиевна', ''),
    ('Вика', 'ИСП-223п', 'Светлана Георгиевна', ''),
    ('Вера', 'ИСП-223п', 'Светлана Георгиевна', ''),
    ('Иван', 'ИСП-223п', 'Светлана Георгиевна', ''),
    ('Егор', 'ИСП-223п', 'Светлана Георгиевна', '')
]

cursor.executemany('INSERT INTO students (name, group_name, teacher, attendance) VALUES (?, ?, ?, ?)', students)
conn.commit()
conn.close()
