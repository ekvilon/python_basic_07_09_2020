"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionError(ZeroDivisionError):
    def __init__(self, txt='Please never divide by zero otherwise I will bite you'):
        self.txt = txt

    @staticmethod
    def divide(x, y):
        try:
            return x / y
        except ZeroDivisionError:
            raise MyZeroDivisionError()


def read_int(n):
    while True:
        s = input(f'Enter number {n}: ')
        try:
            return int(s)
        except ValueError:
            print('Enter valid number')


if __name__ == '__main__':
    number1 = read_int(1)
    number2 = read_int(2)
    try:
        print(MyZeroDivisionError.divide(number1, number2))
    except MyZeroDivisionError as e:
        print(e.txt)
