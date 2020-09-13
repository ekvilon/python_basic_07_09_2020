"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""

str = input('Enter a string which contains words split by whitespace ')
words = str.split(' ')

for num, word in enumerate(words, 1):
    print(f'{num}. {word[:10]}')
