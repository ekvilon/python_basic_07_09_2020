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


if __name__ == '__main__':
    number1 = read_value('Enter first number ')
    number2 = read_value('Enter second number ')

    try:
        print('Result:', number1 / number2)
    except ZeroDivisionError:
        print('Dividing on zero is prohibited')
