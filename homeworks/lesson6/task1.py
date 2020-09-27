"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
(зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""

from itertools import cycle
from time import sleep, time


class TrafficLightState:
    name = ''
    next_state_name = ''
    duration = 0

    def __init__(self, name, next_state_name, duration):
        self.name = name
        self.next_state_name = next_state_name
        self.duration = duration


class BaseTrafficLight:
    _states = []
    _state = None

    def run(self):
        for state in cycle(self._states):
            if self._state:
                sleep(state.duration)
            self._state = state
            print('New state:', self._state.name)

    def get_current_state(self):
        return self._state


class ThreeColorTrafficLight(BaseTrafficLight):
    _states = (
        TrafficLightState('green', 'yellow', 7),
        TrafficLightState('yellow', 'red', 3),
        TrafficLightState('red', 'green', 6)
    )

    def get_current_color(self):
        return self._state.name if self._state else ''


class SemiThreeColorTrafficLight(ThreeColorTrafficLight):
    _last_switch = 0

    def _set_current_switch_time(self):
        self._last_switch = time()

    def _get_elapsed_switch_time(self):
        return time() - self._last_switch if self._last_switch else 0

    def switch_to(self, color):
        if not self._state:
            if color == self._states[0].name:
                self._state = self._states[0]
                self._set_current_switch_time()
            else:
                raise Exception('Wrong initial color')
        else:
            if self._state.next_state_name == color:
                if self._get_elapsed_switch_time() >= self._state.duration:
                    self._state = next(filter(lambda state: state.name == self._state.next_state_name, self._states))
                    self._set_current_switch_time()
                else:
                    raise Exception('Needed delay has not been expired')
            else:
                raise Exception('Wrong next color')


if __name__ == '__main__':
    # Automatic switching approach 1
    # traffic_light = ThreeColorTrafficLight()
    # traffic_light.run()

    # Semi automatic switching approach 2
    # program will terminate with error if you change right order or time
    semi_traffic_light = SemiThreeColorTrafficLight()
    semi_traffic_light.switch_to('green')
    print(semi_traffic_light.get_current_color())
    sleep(7)
    semi_traffic_light.switch_to('yellow')
    print(semi_traffic_light.get_current_color())
    sleep(3)
    semi_traffic_light.switch_to('red')
    print(semi_traffic_light.get_current_color())
    sleep(6)
    semi_traffic_light.switch_to('green')
    print(semi_traffic_light.get_current_color())
