"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
двух аргументов.
"""


def sum_biggest_numbers_in_list(*args, count: int = 2):
    numbers = sorted(args)

    return sum(numbers[-count:])


def my_func(x, y, z):
    """
    Gets 3 numbers and returns sum of two greatest

    :param x: int
    :param y: int
    :param z: int
    :return: int
    """
    return sum_biggest_numbers_in_list(x, y, z, count=2)


if __name__ == '__main__':
    print('Result:', my_func(4, 10, 1))

