"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""


def fact(number):
    if number < 0:
        raise ValueError('Number is negative')
    result = 1

    for n in range(1, number + 1):
        result = result * n if n > 1 else 1
        yield result
    yield result


def main(value):
    for n, number in enumerate(fact(value), 1):
        if n > value:
            break
        print(number, end=' ')


if __name__ == '__main__':
    main(12)
