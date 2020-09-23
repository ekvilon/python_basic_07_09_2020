"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

from statistics import mean
from json import dump
from homeworks.lesson5.utils.fs import get_filename

if __name__ == '__main__':
    try:
        with open(get_filename(__file__, 'task7_file.txt'), 'r', encoding='UTF-8') as file:
            companies = {}
            while line := file.readline():
                name, type, income, outcome = line.split()
                income = int(income)
                outcome = int(outcome)
                profit = income - outcome
                companies[name] = profit
        with open(get_filename(__file__, 'task7_file.json'), 'w', encoding='UTF-8') as json_file:
            result = [{key: profit for key, profit in companies.items()},
                      {'average_profit': mean([profit for profit in companies.values() if profit > 0])}]
            dump(result, json_file)
    except IOError as e:
        print('Program has got an IO error', e)
