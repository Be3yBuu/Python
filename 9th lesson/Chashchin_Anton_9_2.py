# формула покрытия просто бомба,
# если мы умножим длину на ширину и на массу, то мы получим цифру,
# которая физического смысла не имеет
# использую формулу: длина * ширина * высота * плотность
class Road:
    def __init__(self, length, width, height=0.01):  # 1 см толщиной
        self._length = length
        self._width = width
        self._height = height
        self._mass = self._length * self._width * self._height * 1500

    def mass(self):
        return self._mass


road = Road(5000, 20)  # расчет в метрах
print(road.mass, 'кг')
