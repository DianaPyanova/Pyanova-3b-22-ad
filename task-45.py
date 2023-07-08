file_name = str(input('Введите имя файла: '))
try:
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
except Exception:
    print('Ошибка')
    print('Завершение программы')