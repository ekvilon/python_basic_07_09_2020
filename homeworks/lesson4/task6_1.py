"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

import argparse
from itertools import count

parser = argparse.ArgumentParser(description='Generates numbers starting from specified')
parser.add_argument('start', metavar='S', type=int, nargs=1,
                    help='Starting from')
parser.add_argument('limit', metavar='L', type=int, nargs='?',
                    help='Numbers count limit', default=3)


def generate(start, limit):
    end = start + limit - 1

    for number in count(start):
        print(number)
        if number == end:
            break


if __name__ == '__main__':
    args = parser.parse_args()
    generate(args.start[0], args.limit)
