from games.controls.control import TurtleControl


class TurtleTextControl(TurtleControl):
    text: str = ''
    size: int = 12
    font: str = 'Arial'
    style: str = 'normal'
    align: str = ''
    valign: str = ''

    def __init__(self, text: str = '', size: int = 12, font: str = 'Arial', style: str = 'normal', align: str = 'left',
                 valign: str = 'bottom',
                 **kwargs):
        self.text = text
        self.size = size
        self.font = font
        self.style = style
        self.align = align
        self.valign = valign
        super().__init__(**kwargs)

    def render(self):
        self._turtle.clear()
        super().render()
        if self.align == 'center':
            self._turtle.setx(self.x + self.width / 2)
        elif self.align == 'right':
            self._turtle.setx(self.x + self.width)
        if self.valign == 'top':
            self._turtle.sety(self.y - self.size)
        elif self.valign == 'center':
            self._turtle.sety(self.y - self.height / 2 - self.size / 2)
        self._turtle.write(self.text, align=self.align, font=(self.font, self.size, self.style))
        self._turtle.hideturtle()
