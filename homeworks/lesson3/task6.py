"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с
прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово
состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(s: str) -> str:
    """
    Makes first letter of string capital

    :param s: str
    :return: str
    """
    return s.capitalize()


def main():
    s = input('Enter text with words surrounded by whitespaces ')
    words = s.split()
    print(' '.join([int_func(word) for word in words]))


if __name__ == '__main__':
    main()

