try:
    number = int(input('Введите целое число большее или равное одному: '))
    if number < 1:
        print('Введите число большее или равное одному!')
    summ = sum(range(1, number + 1))
    print(f'Сумма чисел от 1 до {number} равна {summ}')
except ValueError:
    print('Ошибка: Введенно не целое число')