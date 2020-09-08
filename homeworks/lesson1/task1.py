"""
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.
"""

x = 47.0
y = 7
z = 47.0 * 7
result = 'x * y = ' + str(z)

print(result)

user_name = input('Enter your name ')
print('Hello,', user_name)

while (desired_salary := input('Enter your desired salary ')) and not desired_salary.isnumeric():
    print('Wrong number, try again')

print('Your desired salary is', desired_salary)
