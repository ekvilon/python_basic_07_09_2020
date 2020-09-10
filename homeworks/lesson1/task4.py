"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
while и арифметические операции.
"""

while (number := input('Enter number ')) and not number.isnumeric():
    print('Wrong number, try again')

number = int(number)
max_digit = 0

while (digit := number % 10) and digit:
    number //= 10
    if digit > max_digit:
        max_digit = digit

print('Max digit:', max_digit)
