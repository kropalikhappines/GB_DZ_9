class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, *args):
        super(Pen, self).__init__(*args)

    def draw(self):
        print(f'Метод ручки {self.title}')


class Pencil(Stationery):
    def __init__(self, *args):
        super(Pencil, self).__init__(*args)

    def draw(self):
        print(f'Метод ручки {self.title}')


class Handle(Stationery):
    def __init__(self, *args):
        super(Handle, self).__init__(*args)

    def draw(self):
        print(f'Метод ручки {self.title}')


stationary = Stationery('stationary')
stationary.draw()

pen = Pen('pen')
pen.draw()

pencil = Pencil('Pencil')
pencil.draw()

handle = Handle('Handle')
handle.draw()
