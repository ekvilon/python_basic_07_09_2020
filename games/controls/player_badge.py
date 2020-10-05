from games.controls.box import TurtleBoxControl
from games.controls.horizontal_card_render import HorizontalCardRender
from games.controls.image import TurtleImageControl
from games.controls.text import TurtleTextControl


class TurtlePlayerBadgeControl:
    def __init__(self, x: float = 10, y: float = 10):
        self.x = x
        self.y = y
        self._name = ''
        self._avatar = ''
        self._bet = 0
        self._status = ''
        self._is_active = False
        self.__cards = []
        self.__cards_render = None
        self.__badge_background = None
        self.__image = None
        self.__name = None
        self.__bet = None
        self.__status = None

    def render(self):
        # todo - fix background re-creating
        self.__badge_background = TurtleBoxControl(width=310, height=135, x=self.x, y=self.y, anchor=(0, 1),
                                                   background_color=f'{"white" if self._is_active else ""}')

        # todo - fix image re-creating
        self.__image = TurtleImageControl(image=self._avatar, x=5, y=5, anchor=(0, 1),
                                          parent=self.__badge_background)

        if not self.__name:
            self.__name = TurtleTextControl(text=self._name, x=5, y=5, anchor=(1, 1), style='bold', valign='center',
                                            width=165, height=40, background_color='', parent=self.__badge_background)

        if not self.__bet:
            self.__bet = TurtleTextControl(text=f'Bet: {self._bet}', x=5, y=50, anchor=(1, 1), valign='center',
                                           width=165, height=25, background_color='', parent=self.__badge_background)

        if not self.__status:
            self.__status = TurtleTextControl(text=self._status, x=5, y=80, anchor=(1, 1), valign='center',
                                              width=165, height=25, background_color='', parent=self.__badge_background)

        # todo - fix cards re-creating
        if len(self.__cards) > 0:
            self.__cards_render = HorizontalCardRender(gutter=5)
            self.__cards_render.push_card(*self.__cards, new_size=(50, 70))

        self.__badge_background.render()
        self.__image.render()
        self.__name.render()
        self.__bet.render()
        self.__status.render()
        if self.__cards_render:
            self.__cards_render.render(x=self.__badge_background.src_x + self.__image.width + 15,
                                       y=self.__badge_background.src_y + self.__badge_background.height - 15,
                                       anchor=(0, 1))

    def activate(self):
        self._is_active = True
        self.render()

    def deactivate(self):
        self._is_active = False
        self.render()

    def set_cards(self, cards):
        self.__cards = cards
        self.render()

    def set_name(self, name):
        self._name = name

    def set_avatar(self, avatar):
        self._avatar = avatar

    def set_bet(self, bet):
        self._bet = bet
        if self.__bet:
            self.__bet.text = f'Bet: {self._bet}'
            self.__bet.render()

    def set_status(self, status):
        self._status = status
        if self.__status:
            self.__status.text = self._status
            self.__status.render()

    def show(self):
        self.__badge_background.set_visibility(True)
        self.__image.set_visibility(True)
        self.__name.set_visibility(True)
        self.__bet.set_visibility(True)
        self.__status.set_visibility(True)

    def hide(self):
        self.__badge_background.set_visibility(False)
        self.__image.set_visibility(False)
        self.__name.set_visibility(False)
        self.__bet.set_visibility(False)
        self.__status.set_visibility(False)
