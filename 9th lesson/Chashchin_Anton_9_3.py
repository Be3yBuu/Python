full_income = {"wage": 390, "bonus": 100}


class Worker:
    def __init__(self):
        self.name = 'Ivan'
        self.surname = 'Ivanov'
        self.position = 'director'
        self._income = full_income['wage']


class Position(Worker):
    def __init__(self):
        super().__init__()
        self.full_income = full_income

    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self.full_income['wage'] + self.full_income['bonus']


x = Position()
print(x._income, x.name, x.surname, x.position)
print(Position.get_full_name(x))
print(Position.get_total_income(x))
