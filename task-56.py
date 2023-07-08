try:
    file_name = input('Введите название файла: ')
    with open(file_name, 'r') as file:
        text = file.read()

    import collections
    words = text.split()
    counter = collections.Counter(words)
    most_common = counter.most_common()[0]

    print(most_common)
except FileNotFoundError:
    print('Файл не найден')