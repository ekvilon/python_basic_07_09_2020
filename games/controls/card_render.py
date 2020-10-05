from games.controls.image import TurtleImageControl
from games.entities import Card


class CardRender:
    def __init__(self, card: Card, **kwargs):
        self._control = TurtleImageControl(image=card.get_card_image(), **kwargs)

    @property
    def width(self):
        return self._control.width

    @property
    def height(self):
        return self._control.height

    def render(self, x: float, y: float, anchor: (0, 0)):
        self._control.src_x = x
        self._control.src_y = y
        self._control.anchor = anchor
        self._control.render()