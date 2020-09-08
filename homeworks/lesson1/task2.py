"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

while (seconds := input('Enter seconds ')) and not seconds.isnumeric():
    print('Wrong number, try again')

seconds = int(seconds)
hours = seconds // 3600
minutes = seconds % 3600 // 60
seconds = seconds % 60

print(f'Time in hh:mm:ss format is {hours:02}:{minutes:02}:{seconds:02}')
