import os

directory = input('Введите путь к директории: ')
extension = input('Введите расширение файла: ')

try:
    for roots, dirs, files in os.walk(directory):
        for file in files:
            if extension in file:
                print(file)
except FileNotFoundError:
    print('Директория не найдена')