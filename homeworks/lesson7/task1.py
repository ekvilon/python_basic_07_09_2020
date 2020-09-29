"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, elements: [[int]]):
        self.elements = elements

    def __add__(self, other):
        rows = len(self.elements)
        return Matrix(map(lambda row: map(sum, zip(self.elements[row], other.elements[row])), range(rows)))

    def __str__(self):
        return '\n'.join(map(lambda row: ' '.join(map(lambda number: str(number), row)), self.elements))


if __name__ == '__main__':
    print('Matrix')
    print('-' * 10)
    m = Matrix([[1, 2], [3, 4], [5, 6]])
    print(m)
    print('Matrix 2')
    print('-' * 10)
    m2 = Matrix([[17, 18], [7, 10], [5, -2]])
    print(m2)
    print('Matrix addiction')
    print('-' * 10)
    print(m + m2)

