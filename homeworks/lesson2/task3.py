"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""

months = {(12, 1, 2): 'winter', (3, 4, 5): 'spring', (6, 7, 8): 'summer', (9, 10, 11): 'autumn'}
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

for key, value in months.items():
    if month in key:
        print('You have entered month of', value)
