class Car:
    def __init__(self):
        self.speed = 40
        self.color = 'red'
        self.name = 'VW Polo'
        self.is_police = False

    def go(self):
        return f'{self.name} have started moving'

    def stop(self):
        return f'{self.name} have stopped'

    def turn(self, direction='left'):
        return f'{self.name} have just turned {direction}'

    def show_speed(self):
        return f'{self.name} is moving with speed "{self.speed}"'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return 'Warning, speeding'
        else:
            return f'{self.name} is moving with speed "{self.speed}"'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Warning, speeding ({self.speed})'
        else:
            return f'{self.name} is moving with speed "{self.speed}"'


class PoliceCar(Car):
    pass


town_car = TownCar()
work_car = WorkCar()

print(town_car.show_speed())
print(work_car.show_speed())
work_car.speed = 100
print(work_car.show_speed())
