import random

array = []
for i in range(random.randint(1, 10)):
    array.append(random.randint(1, 10))
print(sum(array))