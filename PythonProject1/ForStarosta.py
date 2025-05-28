import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class AttendanceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Приложение для отслеживания посещаемости')
        self.geometry('450x400')

        self.conn = sqlite3.connect('students.db')
        self.cursor = self.conn.cursor()

        self.create_widgets()

        fixed_group = "ИСП-223а"  # Здесь укажите нужную группу
        self.load_students(fixed_group)

    def create_widgets(self):
        self.students_frame = tk.Frame(self)
        self.students_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.save_button = tk.Button(self, text='Сохранить', command=self.save_attendance)
        self.save_button.pack(pady=10)

    def load_students(self, group_name):
        for widget in self.students_frame.winfo_children():
            widget.destroy()

        self.cursor.execute(
            'SELECT id, name, group_name, teacher, attendance FROM students WHERE group_name = ?',
            (group_name,)
        )
        self.students = self.cursor.fetchall()

        self.attendance_vars = {}

        tk.Label(self.students_frame, text='Студент', font=('Arial', 12, 'bold')).grid(row=0, column=0, sticky='w', padx=5, pady=5)
        tk.Label(self.students_frame, text='Группа', font=('Arial', 12, 'bold')).grid(row=0, column=1, sticky='w', padx=5, pady=5)
        tk.Label(self.students_frame, text='Посещаемость', font=('Arial', 12, 'bold')).grid(row=0, column=2, sticky='w', padx=5, pady=5)

        for i, (student_id, name, group_name, teacher, attendance) in enumerate(self.students, start=1):
            tk.Label(self.students_frame, text=name).grid(row=i, column=0, sticky='w', padx=5, pady=2)
            tk.Label(self.students_frame, text=group_name).grid(row=i, column=1, sticky='w', padx=5, pady=2)

            display_value = attendance if attendance in ('б', 'у', 'н') else ''

            var = tk.StringVar(value=display_value)
            combo = ttk.Combobox(self.students_frame, textvariable=var, width=5, state='readonly')
            combo['values'] = ('', 'б', 'у', 'н')
            combo.grid(row=i, column=2, sticky='w', padx=5, pady=2)

            self.attendance_vars[student_id] = var

    def save_attendance(self):
        for student_id, var in self.attendance_vars.items():
            val = var.get()
            if val not in ('', 'б', 'у', 'н'):
                messagebox.showerror('Ошибка', f'Неверное значение посещаемости для студента с ID {student_id}')
                return
            self.cursor.execute('UPDATE students SET attendance = ? WHERE id = ?', (val, student_id))
        self.conn.commit()
        messagebox.showinfo('Сохранено', 'Посещаемость сохранена')

    def on_closing(self):
        self.conn.close()
        self.destroy()

if __name__ == '__main__':
    app = AttendanceApp()
    app.protocol('WM_DELETE_WINDOW', app.on_closing)
    app.mainloop()
