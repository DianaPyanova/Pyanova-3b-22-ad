import sqlite3

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movies
                  (name TEXT, genre TEXT, rating INTEGER)''')

movies = [('Фильм1', 'Ужасы', 9.5), ('Фильм2', 'Комедии', 8.9), ('Фильм3', "Драма", 6.7), ('Фильм4', 'Комедии', 8.8)]
cursor.executemany('INSERT INTO movies VALUES (?, ?, ?)', movies)
conn.commit()

cursor.execute('SELECT * FROM movies WHERE genre = "Комедии"')
movies_comedy = cursor.fetchall()
for movie in movies_comedy:
    print(f'Название: {movie[0]}, Жанр: {movie[1]}, Рейтинг: {movie[2]}')
conn.close()