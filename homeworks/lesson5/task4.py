"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

from homeworks.lesson5.utils.fs import get_filename

localizations = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

if __name__ == '__main__':
    try:
        changed_lines = list()

        with open(get_filename(__file__, 'task4_source.txt'), 'r', encoding='UTF-8') as file:
            while line := file.readline():
                changed_lines.append(' '.join([word.replace(word, localizations.get(word, word))
                                               for word in line.split()]))
        with open(get_filename(__file__, 'task4_destination.txt'), 'w', encoding='UTF-8') as new_file:
            new_file.writelines('\n'.join(changed_lines))
    except IOError as e:
        print('Program has got an IO error', e)
