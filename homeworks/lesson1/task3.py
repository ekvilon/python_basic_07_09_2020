"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""

while (number := input('Enter number ')) and not number.isnumeric():
    print('Wrong number, try again')

number = int(number)
temp = number
digits = 0

while temp:
    digits += 1
    temp //= 10

double_multiplier = 10 ** digits + 1
triple_multiplier = 10 ** (digits * 2) + double_multiplier

result = number + (number * double_multiplier) + (number * triple_multiplier)

print('n + nn + nnn =', result)
