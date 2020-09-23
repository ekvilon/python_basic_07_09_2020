"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

from homeworks.lesson5.utils.fs import get_filename

if __name__ == '__main__':
    try:
        with open(get_filename(__file__, 'task1_file.txt'), 'w', encoding='UTF-8') as new_file:
            while line := input('Write your string or hit Enter to finish '):
                new_file.write(line + '\n')
    except IOError as e:
        print('Program has got an IO error', e)
