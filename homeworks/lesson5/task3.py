"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

from statistics import mean
from homeworks.lesson5.utils.types import isfloat
from homeworks.lesson5.utils.fs import get_filename


def read_stuff_from_file():
    with open(get_filename(__file__, 'task3_file.txt'), 'r', encoding='UTF-8') as file:
        lines = filter(lambda cells: len(cells) > 1 and isfloat(cells[-1]),
                       [line.split() for line in file.readlines() if line])
        return list(map(lambda line: {'name': ' '.join(line[0:-1]),
                                      'salary': float(line[-1])},
                        lines))


def print_employees_with_low_salary(employees):
    employees_with_low_salary = [employee['name'] for employee in employees if employee['salary'] < 20_000]
    if employees_with_low_salary:
        print('Employees having low salary:')
        print('-' * 30)
        print('\n'.join(employees_with_low_salary), '\n')


def print_average_salary(employees):
    average_salary = mean([employee['salary'] for employee in employees])
    print('Average salary:')
    print('-' * 30)
    print(f'${average_salary}')


if __name__ == '__main__':
    try:
        stuff = read_stuff_from_file()
        print_employees_with_low_salary(stuff)
        print_average_salary(stuff)
    except IOError as e:
        print('Program has got an IO error', e)
