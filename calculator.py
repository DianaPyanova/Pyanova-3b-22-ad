class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(a, b):
        return a + b

    def subtraction(a, b):
        return a - b

    def multiplication(a, b):
        return a * b

    def division(a, b):
        if b != 0:
            return a / b
        else:
            print('Ошибка: делить на 0 нельзя')
