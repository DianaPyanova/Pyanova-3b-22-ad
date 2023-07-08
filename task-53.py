class Chores:
    def __init__(self, filename):
        self.filename = filename
        self.elements = self.upload()
    def add_elem(self, elem):
        self.elements.append(elem)
        self.save()
    def remove_elem(self, elem):
        if elem in self.elements:
            self.elements.remove(elem)
            self.save()
        else:
            print('Элемент не найден')
    def print_chores(self):
        print('Список домашних дел: ')
        for elem in self.elements:
            print(elem)
    def save(self):
        with open(self.filename, 'w') as file:
            file.write('\n'.join(self.elements))
    def upload(self):
        with open(self.filename, 'r') as file:
            return file.read().splitlines()

chores = Chores('Chores.txt')
chores.print_chores()

chores.add_elem('Постирать вещи')
chores.add_elem('Помыть посуду')
chores.add_elem('Помыть пол')
chores.print_chores()

chores.remove_elem('Помыть пол')
chores.print_chores()