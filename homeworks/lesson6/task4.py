"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
(булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = int(speed)
        self.color = color
        self.name = name

    def go(self):
        print(f'Car {self.name} has started to move')

    def stop(self):
        print(f'Car {self.name} has stopped to move')

    def turn(self, direction):
        print(f'Car {self.name} has turned to', direction)

    def show_speed(self):
        print(f'Car {self.name} has speed {self.speed}')

    def print_speed_limit_message(self):
        print('Man, please slow down!')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            self.print_speed_limit_message()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            self.print_speed_limit_message()


class PoliceCar(Car):
    is_police = True


if __name__ == "__main__":
    town_car = TownCar(60, 'red', 'Toyota Camry')
    sport_car = SportCar(120, 'metallic', 'Porsche Cayenne')
    work_car = WorkCar(50, 'yellow', 'Tractor')
    police_car = PoliceCar(80, 'black', 'Opel Omega')
    print(f'Town car {town_car.name} has color {town_car.color}')
    town_car.go()
    town_car.show_speed()
    print(f'Police car is named "{police_car.name}". Is it police car? {police_car.is_police}')
    work_car.go()
    work_car.turn('right')
    work_car.show_speed()
    sport_car.go()
    sport_car.show_speed()
