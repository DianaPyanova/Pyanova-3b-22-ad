class Schoolboy:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def study(self):
        print(f'Школьник {self.name} учится в {self.grade} классе.')

schoolboy1 = Schoolboy('Иван', 9)
schoolboy1.study()