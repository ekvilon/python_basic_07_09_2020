from turtle import Turtle

from games.screen import Screen


class BaseTurtleControl:
    def __init__(self):
        self.src_x = 0
        self.src_y = 0
        self.width = 0
        self.height = 0
        self.anchor = (0, 0)
        self.background_color = ''
        self.parent = None
        self._hidden_turtle = False
        self._turtle = Turtle()

    def __del__(self):
        self._turtle.clear()
        del self._turtle
        self._turtle = None

    @property
    def x(self):
        x = 0
        left = 0
        right = Screen.get_canvas().winfo_width()
        if self.parent:
            x = self.parent.x
            left = self.parent.x
            right = self.parent.x + self.parent.width
        if self.anchor:
            if self.anchor == (0, 0):
                x = left + (self.src_x if self.src_x else 0)
            if self.anchor == (1, 1):
                x = right - self.width - (self.src_x if self.src_x else 0)
            if self.anchor == (1, 0):
                x = right - self.width - (self.src_x if self.src_x else 0)
            if self.anchor == (0, 1):
                x = left + (self.src_x if self.src_x else 0)
        else:
            if self.src_x:
                x += self.src_x
        return x

    @property
    def y(self):
        y = 0
        bottom = 0
        top = Screen.get_canvas().winfo_height()
        if self.parent:
            y = self.parent.y
            bottom = self.parent.y - self.parent.height
            top = self.parent.y
        if self.anchor:
            if self.anchor == (0, 0):
                y = bottom + self.height + (y if y else 0)
            if self.anchor == (1, 1):
                y = top - (self.src_y if self.src_y else 0)
            if self.anchor == (1, 0):
                y = bottom + self.height + (self.src_y if self.src_y else 0)
            if self.anchor == (0, 1):
                y = top - (self.src_y if self.src_y else 0)
        else:
            if self.src_y:
                y += self.src_y
        return y

    def set_visibility(self, is_visible):
        if is_visible:
            self.render()
        else:
            self._turtle.clear()

    def render(self):
        if self._hidden_turtle:
            self._turtle.hideturtle()
        self._turtle.setpos(self.x, self.y)
        self._turtle.fillcolor(self.background_color)
        self._turtle.begin_fill()
        self._turtle.begin_poly()
        self._turtle.setpos(self.x + self.width, self.y)
        self._turtle.setpos(self.x + self.width, self.y - self.height)
        self._turtle.setpos(self.x, self.y - self.height)
        self._turtle.end_poly()
        self._turtle.end_fill()

