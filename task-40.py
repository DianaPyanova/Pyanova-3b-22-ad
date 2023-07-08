try:
    with open('test.txt', 'r') as file:
        print('Файл существует')
except FileNotFoundError:
    print('Файл не найден')