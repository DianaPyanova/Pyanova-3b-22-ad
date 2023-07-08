try:
    numbers = input('Введите список целых чисел через запятую: ')
    numbers_list = [int(num) for num in numbers.split(',')]
    min_number = min(numbers_list)
    print('Минимальное число:', min_number)
except ValueError:
    print('Ошибка: Введенны не целые числа')