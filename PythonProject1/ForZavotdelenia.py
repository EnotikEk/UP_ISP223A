import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class AttendanceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Приложение для отслеживания посещаемости')
        self.geometry('450x400')

        # Подключаемся к базе один раз при старте
        self.conn = sqlite3.connect('students.db')
        self.cursor = self.conn.cursor()

        self.create_widgets()
        self.load_groups()

    def create_widgets(self):
        # Фрейм для выбора группы
        group_frame = tk.Frame(self)
        group_frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(group_frame, text='Выберите группу:', font=('Arial', 12)).pack(side=tk.LEFT)

        self.group_var = tk.StringVar()
        self.group_combo = ttk.Combobox(group_frame, textvariable=self.group_var, state='readonly')
        self.group_combo.pack(side=tk.LEFT, padx=5)
        self.group_combo.bind('<<ComboboxSelected>>', self.on_group_selected)

        # Фрейм для списка студентов
        self.students_frame = tk.Frame(self)
        self.students_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Кнопка сохранения
        self.save_button = tk.Button(self, text='Сохранить', command=self.save_attendance)
        self.save_button.pack(pady=10)

    def load_groups(self):
        # Получаем список уникальных групп из БД
        self.cursor.execute('SELECT DISTINCT group_name FROM students ORDER BY group_name')
        groups = [row[0] for row in self.cursor.fetchall()]
        if not groups:
            groups = ['']

        self.group_combo['values'] = groups
        if groups:
            self.group_combo.current(0)
            self.load_students(groups[0])

    def on_group_selected(self, event):
        selected_group = self.group_var.get()
        self.load_students(selected_group)

    def load_students(self, group_name):
        for widget in self.students_frame.winfo_children():
            widget.destroy()

        # Запрос с WHERE для выбранной группы
        self.cursor.execute(
            'SELECT id, name, group_name, teacher, attendance FROM students WHERE group_name = ?',
            (group_name,)
        )
        self.students = self.cursor.fetchall()

        self.attendance_vars = {}

        # Заголовки таблицы
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
