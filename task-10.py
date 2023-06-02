class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def personal_data(self):
        print(f'Человека зовут {self.name} и его возраст составляет {self.age} лет')