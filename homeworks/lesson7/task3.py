"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения
до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод
позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: *****\n*****\n*****.
"""


class Cell:
    def __init__(self, cells_count):
        self.cells_count = cells_count

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise Exception('You should perform this operation on Cell')
        return Cell(self.cells_count + other.cells_count)

    def __sub__(self, other):
        if not isinstance(other, self.__class__):
            raise Exception('You should perform this operation on Cell')
        result = self.cells_count - other.cells_count
        if result < 0:
            raise Exception('Result should be 0 or positive')
        return Cell(result)

    def __mul__(self, other):
        if not isinstance(other, self.__class__):
            raise Exception('You should perform this operation on Cell')
        return Cell(self.cells_count * other.cells_count)

    def __floordiv__(self, other):
        if not isinstance(other, self.__class__):
            raise Exception('You should perform this operation on Cell')
        return Cell(self.cells_count // other.cells_count)

    def make_order(self, columns):
        full_rows = self.cells_count // columns
        additional_cells = self.cells_count % columns
        result = '\n'.join(map(lambda idx: '*' * columns, range(full_rows)))
        if additional_cells > 0:
            result += '\n' + '*' * additional_cells
        return result


if __name__ == '__main__':
    c = Cell(5)
    c2 = Cell(2)
    c3 = c + c2
    print(c3.cells_count)
    c3 = c - c2
    print(c3.cells_count)
    c3 = c * c2
    print(c3.make_order(4))
    c3 = c // c2
    print(c3.cells_count)
    c3 = c2 - c
