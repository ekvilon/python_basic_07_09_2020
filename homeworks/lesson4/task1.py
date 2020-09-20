"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

import argparse

parser = argparse.ArgumentParser(description='Calculates salary')
parser.add_argument('spent_hours', metavar='H', type=int, nargs=1,
                    help='Spent hours')
parser.add_argument('rate_per_hour', metavar='R', type=int, nargs=1,
                    help='Rate per hour')
parser.add_argument('bonus', metavar='B', type=int, nargs=1,
                    help='Bonus')


def calculate():
    args = parser.parse_args()
    spent_hours, rate_per_hour, bonus = [getattr(args, arg)[0] for arg in vars(args)]
    result = (spent_hours * rate_per_hour) + bonus
    print(f'Salary is: {result}$')


if __name__ == '__main__':
    calculate()
