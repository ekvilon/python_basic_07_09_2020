"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и
снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа
вводится специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


if __name__ == '__main__':
    total_sum = 0
    while True:
        terminate = False
        s = input('Enter numbers separated by whitespace or "q" to finish ')
        values = s.split()
        for value in values:
            if value.lower() == 'q':
                terminate = True
                break
            try:
                number = int(value)
                total_sum += number
            except ValueError:
                print(f'Skipping {value}: wrong format')
        print('Current sum:', total_sum)
        if terminate:
            break

