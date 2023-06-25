num = input("Список чисел: ").split()
num = [int(num) for num in num]

min = sorted(num)
print("Два наименьших значения списка: ", min[0], min[1])