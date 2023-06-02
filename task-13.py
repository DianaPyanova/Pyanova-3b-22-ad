class BankAccount:
    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def withdraw_funds(self, amount):
        self.balance -= amount
        print(self.name, 'Вы сняли', amount, 'рублей.\n', 'Остаток на счете:', self.balance)

    def top_up_funds(self, amount):
        self.balance += amount
        print(self.name, 'Вы пополнили счет на', amount, 'рублей.\n', 'Сумма на счете:', self.balance)
