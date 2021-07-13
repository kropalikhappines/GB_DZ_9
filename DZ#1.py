import time

class TrafficLigth:
    def __init__(self):

        self.duration_color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 5}
        for color, durat in self.duration_color.items():
            print(color)
            time.sleep(durat)



traffic = TrafficLigth()

# ------------------------------

class TrafficLight:
    def running(self, color, duration):
        self.color = color
        self.duration = duration
        print(f'Горит {self.color}, осталось {self.duration}')
        time.sleep(self.duration)

traffic_light = TrafficLight()

traffic_light.running('Красный', 7)
traffic_light.running('Желтый', 2)
traffic_light.running('Зеленый', 5)

# -------------------------------------------------------

class TrafficLight:
    __color = ''
    def running(self):
        for col, durat in {'Красный': 7, 'Желтый': 2, 'Зеленый': 5}.items():
            self.__color = col
            self.duration = durat
            print(f'Горит {self.__color}, осталось {self.duration} секунд!')
            time.sleep(self.duration)


traf = TrafficLight()
traf.running()