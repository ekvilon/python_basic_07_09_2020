"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

from homeworks.lesson5.utils.fs import get_filename

if __name__ == '__main__':
    try:
        with open(get_filename(__file__, 'task6_file.txt'), 'r', encoding='UTF-8') as file:
            subjects = {}
            while line := file.readline():
                *subject, str_hours = line.split(':')
                subject = ' '.join(subject)
                hours = 0
                for part in str_hours.split(' '):
                    if part and part != '—':
                        value, _ = part.split('(')
                        hours += int(value)
                subjects[subject] = hours
            print(subjects)
    except IOError as e:
        print('Program has got an IO error', e)
