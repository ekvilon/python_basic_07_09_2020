"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
двух аргументов.
"""


def sum_biggest_numbers(*args: [int], amount: int = 2) -> int:
    """
    Takes any count of numbers and return sum of biggest in specified amount

    :param args:
    :param amount:
    :return:
    """
    numbers = sorted(args)

    return sum(numbers[-amount:])


def my_func(x: int, y: int, z: int) -> int:
    """
    Gets 3 numbers and returns sum of two greatest

    :param x: int
    :param y: int
    :param z: int
    :return: int
    """
    return sum_biggest_numbers(x, y, z, amount=2)


if __name__ == '__main__':
    print('Result:', my_func(4, 10, 1))

