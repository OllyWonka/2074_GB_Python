class Worker:
    name: str
    surname: str
    position: str
    _income: dict = {'wage': 0.0, 'bonus': 1.0}

    def __init__(self, name: str, surname: str, position: str,
                 income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self) -> str:
        return f'{self.name} {self.surname}'

    def get_total_income(self) -> int:
        return self._income['wage'] + self._income['bonus']


if __name__ == '__main__':
    welder = Position('Иван', 'Васильев', 'сварщик',
                      {'wage': 50000, 'bonus': 15000})
    driver = Position('Петр', 'Николаев', 'водитель',
                      {'wage': 30000, 'bonus': 7500})
    scientist = Position('Геннадий', 'Разумов', 'ученый',
                         {'wage': 150000, 'bonus': 25000})
    print(welder.get_full_name(),
          welder.get_total_income())
    print(driver.get_full_name(),
          driver.get_total_income())
    print(scientist.get_full_name(),
          scientist.get_total_income())
