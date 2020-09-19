"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def read_value(prompt='Enter number ', type_constructor=int, allow_empty=False):
    while True:
        value = input(prompt)
        try:
            # little cheat xD
            if not allow_empty and not value:
                raise ValueError
            if type_constructor == str:
                return value
            value = type_constructor(value)
            return value
        except ValueError:
            print('Please enter correct value')


def divide_two_numbers(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('Dividing on zero is prohibited')


if __name__ == '__main__':
    x = read_value('Enter first number ')
    y = read_value('Enter second number ')
    result = divide_two_numbers(x, y)

    # result of division can't be 0 or None
    if result:
        print('Result:', x / y)
