class Stationery:
    def __init__(self, name):
        self.title = name

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title}\'s Draw')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} is Drawing')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} is going to Draw ')


stationary = Stationery('stat')
pen = Pen('pen')
pencil = Pencil('pencil')
handle = Handle('handle')
stationary.draw()
pen.draw()
pencil.draw()
handle.draw()
