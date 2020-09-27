"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

ASPHALT_THICKNESS = 7.0
ASPHALT_MASS_OF_SQUARE_METER = 30.0


class Road:
    _length = 0.0
    _width = 0.0

    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)

    def get_mass_of_asphalt(self):
        return self._length * self._width * ASPHALT_THICKNESS * ASPHALT_MASS_OF_SQUARE_METER


if __name__ == "__main__":
    road = Road(100, 5)
    mass = road.get_mass_of_asphalt()
    assert mass == (100.0 * 5.0 * ASPHALT_THICKNESS * ASPHALT_MASS_OF_SQUARE_METER), "masses should match"
    print(f'Road mass is {mass} ton')

