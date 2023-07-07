import sqlite3

conn = sqlite3.connect('employees.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (name TEXT, post TEXT, salary INTEGER)''')

employees = [('Иван', 'Директор', 70), ('Сергей', 'Менеджер', 50), ('Дмитрий', "Менеджер", 50), ('Инна', 'Менеджер', 50)]
cursor.executemany('INSERT INTO employees VALUES (?, ?, ?)', employees)
conn.commit()

cursor.execute('SELECT * FROM employees WHERE post = "Менеджер"')
employees_manager = cursor.fetchall()
for employee in employees_manager:
    print(f'Сотрудник: {employee[0]}, должность: {employee[1]}, зарплата: {employee[2]} тысяч рублей')
conn.close()