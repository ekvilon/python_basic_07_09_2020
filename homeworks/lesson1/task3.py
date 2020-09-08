"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""

while (number := input('Enter number ')) and not number.isnumeric():
    print('Wrong number, try again')

number = int(number)
result = number + number * 11 + number * 111

print('n + nn + nnn =', result)
