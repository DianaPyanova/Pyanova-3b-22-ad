from typing import List, Tuple

def maxValueAndOrderOfNumbers(numbers: List[int]) -> Tuple[int, int]:
    max_value = float('-inf') # Инициализируем переменную максимального значения как отрицательную бесконечность
    max_index = -1 # Инициализируем переменную порядкового номера максимального значения

    for i, num in enumerate(numbers): # Перебор
        if num > max_value:
            max_value = num
            max_index = i

    return max_value, max_index

# Пример использования
sequence = input("Введите последовательность чисел, разделенных пробелами: ")
numbers = list(map(int, sequence.split()))
max_value, max_index = maxValueAndOrderOfNumbers(numbers)

print("Наибольшее значение:", max_value)
print("Порядковый номер:", max_index + 1)