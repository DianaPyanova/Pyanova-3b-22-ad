def calc(num1, num2, operation):
    if operation == 'сложение':
        return num1 + num2
    elif operation == 'вычитание':
        return num1 - num2
    elif operation == 'умножение':
        return num1 * num2
    elif operation == 'деление':
        return num1 / num2
    else:
        print('Нет такой операции')
        return None


number1 = float(input())
number2 = float(input())
oper = str(input())
print(calc(number1, number2, oper))