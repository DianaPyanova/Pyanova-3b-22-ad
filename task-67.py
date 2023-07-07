import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS books
                  (name TEXT, author TEXT, year INTEGER)''')

books = [('Книга1', 'Автор1', 1885), ('Книга2', 'Автор2', 1990), ('Книга3', 'Автор3', 2020), ('Книга4', 'Автор4', 2009)]
cursor.executemany('INSERT INTO books VALUES (?, ?, ?)', books)
conn.commit()

cursor.execute('SELECT * FROM books WHERE year > 2000')
books_after_2000 = cursor.fetchall()
for book in books_after_2000:
    print(f'Название: {book[0]}, Автор: {book[1]}, Год издания: {book[2]}')
conn.close()