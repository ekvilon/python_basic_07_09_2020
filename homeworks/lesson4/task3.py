"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""


def main():
    result = [number for number in range(20, 240) if not number % 20 or not number % 21]
    print(result)


if __name__ == '__main__':
    main()
