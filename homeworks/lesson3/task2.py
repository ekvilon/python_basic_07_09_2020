"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой.
"""


def create_user_data(first_name: str,
                     last_name: str,
                     dob: str,
                     city: str,
                     email: str,
                     phone: str):
    return first_name, last_name, dob, city, email, phone


def print_user_data(user):
    first_name, last_name, dob, city, email, phone = user
    print(
        f'User profile - name: {first_name} {last_name}, date of birth: {dob}, ' +
        f'city of living: {city}, email: {email}, phone: {phone}'
    )


def main():
    user = create_user_data(
        first_name='Joe',
        last_name='Doe',
        dob='01.01.1970',
        city='London',
        email='joe.doe@gmail.com',
        phone='+44 1632 960492')
    print_user_data(user)


if __name__ == '__main__':
    main()

