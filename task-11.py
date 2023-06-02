class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def dog_info(self):
        print("Breed:", self.breed, "\nName:", self.name, "\nAge:", self.age)