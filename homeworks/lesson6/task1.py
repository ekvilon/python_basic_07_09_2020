"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
(зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""

from time import time, sleep


class TrafficLight:
    __current_state = 0
    __next_state = 1
    __states = (('green', 7), ('yellow', 2), ('red', 5), ('yellow', 2))
    __last_switch = time()

    def __init__(self):
        self._set_current_color()

    def running(self):
        while True:
            print(self.__color)
            self._delay()
            self._set_next_state()

    def color(self):
        return self.__color

    def switch_to_color(self, next_color):
        if self.__states[self.__next_state][0] != next_color:
            raise Exception('Wrong next color')
        delay = self._get_current_delay()
        if self._is_needed_time_elapsed(delay):
            self._set_next_state()
            self.__last_switch = time()

    def _set_next_state(self):
        self.__current_state += 1
        if self.__current_state + 1 > len(self.__states):
            self.__current_state = 0
        self._set_current_color()
        self.__next_state = self.__current_state + 1

    def _set_current_color(self):
        self.__color = self.__states[self.__current_state][0]

    def _get_current_delay(self):
        return self.__states[self.__current_state][1]

    def _delay(self):
        delay = self._get_current_delay()

        while True:
            if self._is_needed_time_elapsed(delay):
                self.__last_switch = time()
                break

    def _is_needed_time_elapsed(self, delay):
        return time() - self.__last_switch >= delay


if __name__ == '__main__':
    traffic_light = TrafficLight()

    traffic_light.running()

    # print(traffic_light.color())
    # sleep(7)
    # traffic_light.switch_to_color('yellow')
    # print(traffic_light.color())
    # sleep(2)
    # traffic_light.switch_to_color('red')
    # print(traffic_light.color())
