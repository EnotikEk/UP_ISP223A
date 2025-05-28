from db import *
from ForZavotdelenia import *
import os
import sys

def analiz(entry, entry2, label):
    login = entry.get()
    password = entry2.get()

    conn = sqlite3.connect('Login_Password.db')
    cursor = conn.cursor()

    query = '''SELECT * FROM Login WHERE login = ? AND password = ?'''



    cursor.execute(query, (login, password))
    result = cursor.fetchone()
    conn.close()

    if result and password == '123':
        os.execv(sys.executable, ['python', 'ForZavotdelenia.py'])
    elif result and password == '321':
        os.execv(sys.executable, ['python', 'ForStarosta.py'])
    else:
        label['text'] = 'Вы ввели не правильный логин или пароль'




































# def show_answer(entry, label):
#     a = int(entry.get())
#     s = a + 123
#     label['text'] = s
#
# def show(entry2, label2):
#     a = entry2.get()
#     if a == 'get':
#         label2['text'] = 'Верный пароль'
#     else:
#         label2['text'] = 'Введен не правильный \nпароль'
