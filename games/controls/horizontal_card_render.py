from games.controls.card_render import CardRender
from games.entities import Card


class HorizontalCardRender:
    def __init__(self, align: str = 'left', gutter: int = 20):
        self._cards = []
        self.align = align
        self.__gutter = gutter

    def push_card(self, *cards: [Card], **kwargs):
        self._cards.extend([CardRender(card, **kwargs) for card in cards])

    def render(self, x: float, y: float, anchor: tuple):
        final_x = x
        cards_count = len(self._cards)
        if cards_count > 0:
            if self.align == 'center':
                final_x = x - ((self._cards[0].width * cards_count) + (self.__gutter * cards_count - 1)) / 2
            if self.align == 'right':
                final_x = x - ((self._cards[0].width * cards_count) + (self.__gutter * cards_count - 1))

        for idx, card in enumerate(self._cards):
            card.render(final_x + (idx * (card.width + self.__gutter)), y, anchor)

    def hide(self):
        for card in self._cards:
            card.set_visibility(False)