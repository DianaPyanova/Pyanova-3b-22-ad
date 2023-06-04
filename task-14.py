class Student:
    def __init__(self, name, surname, age, specialization):
        self.name = name
        self.surname = surname
        self.age = age
        self.specialization = specialization

    def student_info(self):
        print(f'{self.name} - {self.surname}, {self.age} лет, {self.specialization}')