from tkinter import *
from prog import *

def toggle_password():
    global show
    if show:
        entry2.config(show='*')
    else:
        entry2.config(show='')
    show = not show

root = Tk()
root.title('asdfasdfa')
root.geometry('300x300')

log = Label(text='Логин')
log.grid(row=0, column=2)

entry = Entry()
entry.grid(row=1, column=2, ipadx=70, ipady=6, padx=5, pady=5, sticky=N)

pas = Label(text='Пароль')
pas.grid(row=2, column=2)

entry2 = Entry(root, show='*')
entry2.grid(row=3, column=2, ipadx=70, ipady=6, padx=5, pady=5, sticky=N)

show = Button(root, text='👀', command=toggle_password)
show.grid(row=3, column=3, ipadx=5, ipady=5)

btn = Button(text='Ввод данных', command=lambda: analiz(entry, entry2, label))
btn.grid(row=4, column=2, ipadx=6, ipady=6, padx=5, pady=5)

label = Label()
label.grid(row=5, column=2, ipadx=6, ipady=6, padx=5, pady=5)

root.mainloop()