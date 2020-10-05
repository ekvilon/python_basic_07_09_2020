from PIL import Image, ImageTk
from tkinter import PhotoImage
from turtle import Shape

from games.controls.control import TurtleControl
from games.screen import Screen


class TurtleImageControl(TurtleControl):
    _key = ''
    _image: PhotoImage = None

    def __init__(self, image: str, **kwargs):
        self._key = f'resources/{image}'
        image = Image.open(self._key)
        new_size = kwargs.get('new_size')
        if new_size:
            image = image.resize(new_size)
        self._image = ImageTk.PhotoImage(image=image)
        Screen.get_screen().addshape(self._key, Shape('image', self._image))
        super().__init__(width=self._image.width(), height=self._image.height(), background_color='', **kwargs)

    def render(self):
        super().render()
        self._turtle.setpos(self.x + self.width / 2, self.y - self.height / 2)
        self._turtle.shape(self._key)
