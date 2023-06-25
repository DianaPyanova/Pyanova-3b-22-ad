string = str(input('Введите строку: '))
list = set(list(string))
for elem in list:
    print(f'{elem} используется {string.count(elem)} раз')