"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def read_value(prompt='Enter int or float ', *types):
    while True:
        value = input(prompt)
        result = None
        for type_constructor in types:
            try:
                result = type_constructor(value)
            except ValueError:
                continue
        if result is None:
            print('Enter correct value')
        else:
            return result


def positive_int(value):
    number = int(value)
    if not (number > 0):
        raise ValueError('It is not positive int')
    return number


def positive_float(value):
    number = float(value)
    if not (number > 0):
        raise ValueError('It is not positive float')
    return number


def negative_int(value):
    number = int(value)
    if not (number < 0):
        raise ValueError('It is not negative int')
    return number


def my_func(x, y):
    return x ** y


def my_func2(x, y):
    x_in_power = x
    for _ in range(0, abs(y) - 1):
        x_in_power *= x_in_power
    return 1 / x_in_power


if __name__ == '__main__':
    real_number = read_value('Enter positive int or float ', positive_int, positive_float)
    power = read_value('Enter negative int ', negative_int)
    print('Result (1 approach):', my_func(real_number, power))
    print('Result (2 approach):', my_func2(real_number, power))

