"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from homeworks.lesson5.utils.fs import get_filename
from random import randint

if __name__ == '__main__':
    try:
        numbers = [randint(1, 10) for number in range(0, 10)]
        with open(get_filename(__file__, 'task5_file.txt'), 'w', encoding='UTF-8') as new_file:
            new_file.write(' '.join([str(number) for number in numbers]))
        with open(get_filename(__file__, 'task5_file.txt'), 'r', encoding='UTF-8') as file:
            sum_of_numbers = 0
            for value in file.readline().split(' '):
                number = int(value)
                sum_of_numbers += number
            assert sum(numbers) == sum_of_numbers, 'sums should match'
            print('Sum of numbers:', sum_of_numbers)
    except IOError as e:
        print('Program has got an IO error', e)
