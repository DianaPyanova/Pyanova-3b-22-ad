def lcm(num1, num2):
    for i in range(2, min(num1, num2)+1):
        if (num1 % i == 0) and (num2 % i == 0):
            return i
    return None


number1 = int(input())
number2 = int(input())
lcm(number1, number2)