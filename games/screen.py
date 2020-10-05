from turtle import Turtle


class Screen:
    @classmethod
    def get_turtle(cls) -> Turtle:
        if not hasattr(cls, '__turtle'):
            turtle = Turtle()
            setattr(cls, '__turtle', turtle)
        return getattr(cls, '__turtle')

    @classmethod
    def get_screen(cls):
        if not hasattr(cls, '__screen'):
            setattr(cls, '__screen', cls.get_turtle().getscreen())
        return getattr(cls, '__screen')

    @classmethod
    def get_canvas(cls):
        return cls.get_screen().getcanvas()

