from games.controls.horizontal_card_render import HorizontalCardRender
from games.entities import Card
from games.screen import Screen


class BoardCardsRender:
    def __init__(self):
        self._render = HorizontalCardRender(align='center')

    def push_card(self, *cards: [Card]):
        self._render.push_card(*cards)

    def render(self):
        canvas = Screen.get_canvas()
        self._render.render(canvas.winfo_width() / 2, canvas.winfo_height() / 2 - 70, (0, 1))