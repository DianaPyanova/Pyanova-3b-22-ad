import calculator

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

result_addition = calculator.addition(a, b)
result_subtraction = calculator.subtraction(a, b)
result_multiplication = calculator.multiplication(a, b)
result_division = calculator.division(a, b)

print(f'Сумма: {result_addition}, разность: {result_subtraction}, умножение: {result_multiplication}, деление: {result_division}')
