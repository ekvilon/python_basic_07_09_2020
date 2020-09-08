"""
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
"""

while (first_day_distance := input('Enter runner first day distance ')) and not first_day_distance.isnumeric():
    print('Wrong number, try again')

while (destination := input('Enter runner destination distance ')) and not destination.isnumeric():
    print('Wrong number, try again')

first_day_distance = int(first_day_distance)
destination = int(destination)
distance = first_day_distance
day = 2

print('1-st day distance:', first_day_distance)

while distance := distance + distance / 10:
    print(f'{day}-th day distance: {distance:.2f}')
    if distance > destination:
        break
    day += 1
