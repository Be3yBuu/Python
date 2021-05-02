# странная формула использована в примере, вообще не понял её смысла
# использую формулу: длина * ширина * высота * плотность
class Road:
    def __init__(self, length, width, height=1):
        self._length = length
        self._width = width
        self._height = height
        self._mass = self._length * self._width * self._height * 0.00233  # мелкозернистый асфальт 2330кг/м^3


road = Road(5000, 20, 5)  # (метр, метр, сантиметр))
print(road._mass, 'тонн')
