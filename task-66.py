import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students
                  (name TEXT, age INTEGER, average_score REAL)''')

students = [('Иван', 18, 3.9), ('Алина', 19, 4.5), ('Мария', 18, 5.0)]
cursor.executemany('INSERT INTO students VALUES (?, ?, ?)', students)
conn.commit()

cursor.execute('SELECT * FROM students')
all_students = cursor.fetchall()
for student in all_students:
    print(f'Студент: {student[0]}, Возраст: {student[1]}, Средний балл: {student[2]}')
conn.close()