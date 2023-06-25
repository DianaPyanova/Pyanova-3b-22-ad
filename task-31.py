from calculator import Calculator

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

result_addition = Calculator.addition(a, b)
result_subtraction = Calculator.subtraction(a, b)
result_multiplication = Calculator.multiplication(a, b)
result_division = Calculator.division(a, b)

print(f'Сумма: {result_addition}, разность: {result_subtraction}, умножение: {result_multiplication}, деление: {result_division}')
