"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    __asphalt_mass_on_square_meter = 30.0

    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)

    def get_mass_of_asphalt(self, thickness: float = 1.0):
        return self._length * self._width * thickness * self.__asphalt_mass_on_square_meter


if __name__ == "__main__":
    road = Road(100.0, 5.0)
    mass = road.get_mass_of_asphalt(2.0)
    print(f'Road mass is {mass} ton')

