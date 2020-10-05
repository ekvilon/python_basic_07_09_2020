"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, real, unreal):
        self._real = real
        self._unreal = unreal

    @property
    def real(self):
        return self._real

    @property
    def unreal(self):
        return self._unreal

    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            raise ValueError('You should add same type')
        return ComplexNumber(self.real + other.real, self.unreal + other.unreal)

    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            raise ValueError('You should multiply same types')
        return ComplexNumber(self.real * other.real - self.unreal * other.unreal,
                             self.unreal * other.real + self.real * other.unreal)

    def __str__(self):
        return f'{self.real if self.real != 0 else ""}{"+" if self.real != 0 and self.unreal > 0 else ""}{self.unreal}i'


if __name__ == '__main__':
    x = ComplexNumber(0, 2)
    y = ComplexNumber(-2, 3)
    print('x', x)
    print('y', y)
    print('addiction', x + y)
    print('multiplication', x * y)

