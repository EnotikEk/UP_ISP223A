from tkinter import *
from prog import *

root = Tk()
root.title('asdfasdfa')
root.geometry('300x250')

entry = Entry(root)
entry.grid(row=0, column=0, columnspan=3)

btn = Button(text='Ввод данных', command=lambda: analiz())
btn.grid(row=1, column=0)

label = Label()
label.grid(row=2, column=0)

entry2 = Entry(root)
entry2.grid(row=0, column=1, padx=3)

btn2 = Button(text='Ввод данных')
btn2.grid(row=1, column=1, padx=3)

label2 = Label()
label2.grid(row=2, column=1, padx=3)

root.mainloop()