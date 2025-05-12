import sqlite3

conn = sqlite3.connect('Login_Password.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Login(
    id INTEGER PRIMARY KEY,
    name TEXT,
    login TEXT, 
    password TEXT,
    post TEXT,
    group_for TEXT )''')

logins = [
    (1, 'Мурина Елена Владимировна', 'isp-23a-123', 'Isp-23a-123', 'завотделения', 'NULL'),
    (2, 'Лукина Екатерина Андреевна', 'isp-23a-12', 'Isp-23a-12', 'староста', 'Исп-223а'),
    (3, 'Да', '123', '123', 'завотделения', 'NULL'),
    (4, 'Нет', '321', '321', 'староста', 'Исп-223а'),
]

for login in logins:
    cursor.execute('SELECT * FROM Login WHERE name = ? AND login = ? AND password = ? AND post = ? AND group_for = ?', (login[1], login[2], login[3], login[4], login[5]))
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO Login (id, name, login, password, post, group_for) VALUES (?, ?, ?, ?, ?, ?)', login)


conn.commit()