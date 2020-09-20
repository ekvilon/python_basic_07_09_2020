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
from itertools import cycle

parser = argparse.ArgumentParser(description='Generates a series of card names specified times')
parser.add_argument('limit', metavar='C', type=int, nargs='?',
                    help='Count', default=3)

card_names = ['jack', 'queen', 'king', 'ace', 'joker']


def generate(limit):
    cards_count = len(card_names)
    end = cards_count * limit

    for idx, card_name in enumerate(cycle(card_names), 1):
        print(idx, card_name)
        if idx == end:
            break


if __name__ == '__main__':
    args = parser.parse_args()
    generate(args.limit)
