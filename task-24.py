class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def presentation(self):
        print(f'Имя сотрудника - {self.name}, возраст сотрудника - {self.age}, зарплата сотрудника - {self.salary}')

employee = Employee('John', 23, 3000)
employee.presentation()