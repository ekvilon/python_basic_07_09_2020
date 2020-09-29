"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
— одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
 соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import abstractmethod


class Cloth:
    def __init__(self, title):
        self.title = title

    @property
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Cloth):
    def __init__(self, title, size):
        self.size = size
        super().__init__(title)

    @property
    def fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Cloth):
    def __init__(self, title, height):
        self.height = height
        super().__init__(title)

    @property
    def fabric_consumption(self):
        return 2 * self.height + 0.3


if __name__ == '__main__':
    coat = Coat('Luis Vuitton', 44)
    suit = Coat('Versace', 1.90)
    print(f'Total fabric consumption is {coat.fabric_consumption + suit.fabric_consumption:.2}')
