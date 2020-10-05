from turtle import Turtle
from typing import Callable

from games.controls.text import TurtleTextControl


class TurtleButtonControl(TurtleTextControl):
    click_handler: Callable = lambda: None

    def __init__(self, click_handler: Callable = lambda: None, **kwargs):
        super().__init__(**kwargs)
        self.click_handler = click_handler
        Turtle.onscreenclick(lambda mouse_x, mouse_y: self.on_click(mouse_x, mouse_y), add=True)

    def on_click(self, x, y):
        if self.visible and self.x <= x <= self.x + self.width and self.y >= y >= self.y - self.height:
            print('hahaha')
