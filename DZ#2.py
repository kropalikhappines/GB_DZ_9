class Road:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError('Не может быть меньше или равно 0')

        self._length = length
        self._width = width


    def mass_calculation(self, weight, thickness):
        if weight <= 0 or thickness <= 0:
            raise ValueError('Не может быть меньше или равно 0')
        return (self._length * self._width * weight * thickness) // 1000



road = Road(20, 5000)
result = road.mass_calculation(25, 5)
print(f'{result} т.')