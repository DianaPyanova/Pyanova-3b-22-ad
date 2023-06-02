class Student:
    def __init__(self, name, surname, grade, marks):
        self.name = name
        self.surname = surname
        self.grade = grade
        self.marks = marks

    def average_mark(self):
        return sum(self.marks) / len(self.marks)
