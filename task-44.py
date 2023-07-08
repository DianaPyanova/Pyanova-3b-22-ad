try:
    with open('test.txt', 'r') as file:
        read_content = file.read()
        print(read_content)
except FileNotFoundError:
    print('Файл не найден')
    print('Завершение программы')