class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

    def income(self):
        return self._income

class Position(Worker):
    def __init__(self, *args):
        super().__init__(*args)

    def get_full_name(self):
        return f'{self.name, self.surname}'

    def get_total_income(self):
        return self.income().get('wage', 0), self.income().get('bonus', 0)

leon = Position('leon', 'leonov','song', 10000, 5000)
print(Position.get_full_name(leon))
print(Position.get_total_income(leon))