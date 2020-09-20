"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from decimal import Decimal
from functools import reduce


def main():
    numbers = [number for number in range(100, 1001) if not number & 1]
    result = reduce(lambda accumulator, number: accumulator * number, numbers)
    print(f'Result is: {Decimal(result):.2E}')


if __name__ == '__main__':
    main()
