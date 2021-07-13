class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')

    def go(self):
        print('Вперед')

    def stop(self):
        print('Остановилась')

    def turn(self, direction):
        print(f'Повернула {direction}')

class TownCar(Car):
    def __init__(self, *args):
        super().__init__(*args)

    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превысили скорость {self.speed}')
        else:
            print(f'Текущая скорость {self.speed}')

class SportCar(Car):
    def __init__(self, *args):
        super().__init__(*args)

class WorkCar(Car):
    def __init__(self, *args):
        super().__init__(*args)

    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превысили {self.speed}')
        else:
            print(f'Текущая скорость {self.speed}')


class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args)


car = TownCar(65, 'Blue', 'Toyota')
car.show_speed()

car1 = WorkCar(40, 'red', 'zhiguli')
car1.show_speed()
car1.go()
car1.turn('Направо')