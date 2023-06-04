def check_number(number: int) -> None:
    for i in range(2, round(number**0.5) + 1):
        if number % i == 0:
            print('Число не является простым')
            return
    print('Число является простым')


num = int(input())
check_number(num)
