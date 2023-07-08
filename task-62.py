class Robot:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def movement(self, time):
        distance = self.speed * time
        print(f'{self.name} прошел {distance} единиц пути за {time} единиц времени')

class FullTrackRobot(Robot):
    def __init__(self, name, speed, territory):
        super().__init__(name, speed)
        self.territory = territory

class WheelRobot(Robot):
    def __init__(self, name, speed, car_brand):
        super().__init__(name, speed)
        self.car_brand = car_brand


robot1 = Robot('Робот Обычный', 3)
robot1.movement(8)

robot2 = FullTrackRobot('Гусеничный Робот', 5, 'Пустыня')
robot2.movement(8)

robot3 = WheelRobot('Робот на колёсах', 10, 'Лада')
robot3.movement(8)