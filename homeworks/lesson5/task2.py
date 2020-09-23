"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

from homeworks.lesson5.utils.fs import get_filename

if __name__ == '__main__':
    try:
        with open(get_filename(__file__, 'task2_file.txt'), 'r', encoding='UTF-8') as file:
            lines_count = 0
            while line := file.readline():
                words_count = len(line.split())
                lines_count += 1
                print(f'{lines_count} line: has {words_count} words')
            print('Lines count:', lines_count)
    except IOError as e:
        print('Program has got an IO error', e)
