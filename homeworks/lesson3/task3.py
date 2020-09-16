"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
двух аргументов.
"""


def my_func(*numbers: [int]):
    """
    Gets 3 numbers and returns sum of two greatest

    :param numbers:
    :return: int
    """
    if len(numbers) != 3:
        raise Exception('You should pass 3 numbers')
    values = list(numbers)
    while len(values) != 2:
        min_number = min(values)
        values.remove(min_number)
    return sum(values)


if __name__ == '__main__':
    print('Result:', my_func(10, 5, 7))

