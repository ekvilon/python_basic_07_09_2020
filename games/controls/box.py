from games.controls.control import TurtleControl


class TurtleBoxControl(TurtleControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._hidden_turtle = True

