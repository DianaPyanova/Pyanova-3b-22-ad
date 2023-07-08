try:
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    print(f'Результат: {a / b}')
except Exception:
    print('Ошибка')
    print('Завершение программы')