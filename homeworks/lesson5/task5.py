"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from homeworks.lesson5.utils.fs import get_filename
from homeworks.lesson5.utils.types import isfloat

if __name__ == '__main__':
    try:
        with open(get_filename(__file__, 'task5_file.txt'), 'w', encoding='UTF-8') as new_file:
            while value := input('Write int or float or hit Enter to finish '):
                if value.isnumeric() or isfloat(value):
                    new_file.write(value + '\n')
                else:
                    print('Wrong number, try again')
        with open(get_filename(__file__, 'task5_file.txt'), 'r', encoding='UTF-8') as file:
            sum_of_numbers = 0
            while value := file.readline():
                number = float(value)
                sum_of_numbers += number
            print('Sum of numbers:', sum_of_numbers)
    except IOError as e:
        print('Program has got an IO error', e)
