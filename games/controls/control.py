from turtle import Turtle
from typing import Union

from games.controls.base import BaseTurtleControl


class TurtleControl(BaseTurtleControl):
    def __init__(self, width: int, height: int, x: Union[int, bool] = False, y: Union[int, bool] = False,
                 anchor: tuple = (0, 0), background_color: str = 'black', parent: BaseTurtleControl = None,
                 new_size: tuple = None):
        super().__init__()
        self.width = width
        self.height = height
        self.src_x = x
        self.src_y = y
        self.anchor = anchor
        self.background_color = background_color
        self.parent = parent
        self._turtle.penup()

    def render(self):
        super().render()

