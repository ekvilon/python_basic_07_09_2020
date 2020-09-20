"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from decimal import Decimal
from functools import reduce


def get_multiplication():
    numbers = [number for number in range(100, 1001) if not number & 1]
    return reduce(lambda accumulator, number: accumulator * number, numbers)


if __name__ == '__main__':
    result = float(Decimal(get_multiplication()).log10())
    assert result == 1207.0668317114541, 'should be equal'

