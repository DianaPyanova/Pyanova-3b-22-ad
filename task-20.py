import random

array = []
for i in range(10):
    array.append(random.randint(1, 100))
print(max(array), min(array))