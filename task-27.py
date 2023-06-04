from random import randint

lst = list([randint(1, 10) for _ in range(randint(2, 10))])
for num in lst:
    if num % 2 == 0:
        print(num)