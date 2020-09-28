"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
описанный метод для каждого экземпляра.
"""


class Stationery:
    __title = 'Запуск отрисовки.'

    def draw(self):
        print(self.__title)


class Pen(Stationery):
    __title = 'Ручка Parker'

    def draw(self):
        print(self.__title, 'рисует уверенно')


class Penсil(Stationery):
    __title = 'Карандаш Eric Krause'

    def draw(self):
        print(self.__title, 'рисует тонко')


class Handle(Stationery):
    __title = 'Маркер Bic'

    def draw(self):
        print(self.__title, 'выделяет текст круто')


if __name__ == '__main__':
    s = Stationery()
    s.draw()
    pen = Pen()
    pen.draw()
    pencil = Penсil()
    pencil.draw()
    handle = Handle()
    handle.draw()
