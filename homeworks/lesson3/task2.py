"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой.
"""

from homeworks.lesson3.task1 import read_value

user_meta = (
    ('firstName', 'First name', 'Enter first name ', str),
    ('lastName', 'Last name', 'Enter last name ', str),
    ('dob', 'Birthday', 'Enter birthday ', str),
    ('city', 'City', 'Enter city ', str),
    ('email', 'Email', 'Enter email ', str),
    ('phone', 'Phone', 'Enter phone ', str)
)


def read_dict(meta):
    obj = {}
    for info in meta:
        field_name, field_title, prompt, constructor = info
        obj[field_name] = field_title, read_value(prompt, constructor)
    return obj


if __name__ == '__main__':
    user = read_dict(user_meta)
    print('\n\nEntered user profile:\n\n')
    for field_name, data in user.items():
        title, value = data
        print(title, value)

