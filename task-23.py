import random

array = []
for i in range(random.randint(1, 10)):
    array.append(random.randint(1, 10))
number = int(input())
if number in array:
    print('Число найдено в массиве')
else:
    print('Число не найдено в массиве')