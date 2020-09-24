"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

from statistics import mean
from homeworks.lesson5.utils.fs import get_filename


def read_stuff_from_file():
    employees = []
    with open(get_filename(__file__, 'task3_file.txt'), 'r', encoding='UTF-8') as file:
        while line := file.readline():
            parts = line.split()
            if len(parts) > 1:
                *name, salary = parts
                employees.append((' '.join(name), int(salary)))
    return employees


def print_employees_with_low_salary(employees):
    employees_with_low_salary = [employee[0] for employee in employees if employee[1] < 20_000]
    if employees_with_low_salary:
        print('Employees having low salary:')
        print('-' * 30)
        print('\n'.join(employees_with_low_salary), '\n')


def print_average_salary(employees):
    average_salary = mean([employee[1] for employee in employees])
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
