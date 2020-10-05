"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    days_in_months = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    def __init__(self, date_str):
        day, month, year = Date.parse_date_str(date_str)
        Date.validate_date(day, month, year)
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def parse_date_str(cls, date_str):
        parts = date_str.split('-')
        if len(parts) != 3:
            raise Exception('Wrong date format. It should be dd-mm-yyyy')
        try:
            day, month, year = map(lambda s: int(s), parts)
        except ValueError as e:
            raise Exception('Wrong value in date string', e)
        return int(day), int(month), int(year)

    @staticmethod
    def validate_date(day, month, year):
        if not year > 0:
            raise Exception('Year should be positive')
        if not 0 < month < 13:
            raise Exception('Month should be in range 1-12')
        is_year_leap = Date.is_year_leap(year)
        Date.validate_day_in_month(is_year_leap, month, day)

    @staticmethod
    def is_year_leap(year):
        if year % 4 == 0:
            return year % 400 == 0 if year % 100 == 0 else True
        else:
            return False

    @classmethod
    def validate_day_in_month(cls, is_year_leap, month, day):
        days = cls.days_in_months[month]
        if month == 2 and is_year_leap:
            days += 1
        if not 0 < day <= days:
            raise Exception(f'Month {month} has {days} days')

    def __str__(self):
        return f'{self.day}-{self.month}-{self.year}'


if __name__ == '__main__':
    # date = Date('30-02-2020')
    date = Date('10-08-2018')
    print(date)
