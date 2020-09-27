"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name = ''
    surname = ''
    position = ''
    income = {}

    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income
        self.income.setdefault('wage', 0)
        self.income.setdefault('bonus', 0)


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self.income['wage'] + self.income['bonus']


if __name__ == "__main__":
    p = Position('Adam', 'Smith', 'director', {'wage': 1_500, 'bonus': 300})
    assert p.get_full_name() == 'Adam Smith'
    assert p.get_total_income() == 1800
    p2 = Position('Joe', 'Doe', 'worker', {'wage': 300})
    assert p2.get_total_income() == 300
    print(f'Name: {p.get_full_name()}, total income: {p.get_total_income()}')
    print(f'Name: {p2.get_full_name()}, total income: {p2.get_total_income()}')