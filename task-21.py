import random

array1, array2 = [], []
for i in range(random.randint(1, 10)):
    array1.append(random.randint(1, 100))
    array2.append(random.randint(1, 100))
array1.extend(array2)