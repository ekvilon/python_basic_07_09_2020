"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""

seasons = ('winter', 'spring', 'summer', 'autumn')

month = None

while True:
    value = input('Enter month number starting from 1 to 12 including ')
    if value.isnumeric():
        value = int(value)
        if 0 < value <= 12:
            month = value
            break
    if month is None:
        print('Enter correct month number')

print(f'Month {month} is in {seasons[month // 3 % 4]}')
