from copy import deepcopy

from games.pocker_utils import get_player_score


class GameData:
    def __init__(self):
        self.bet = 0


class RoundData:
    def __init__(self):
        self.bet = 0
        self.did_check = False
        self.did_fold = False
        self.did_bet = False
        self.did_call = False
        self.did_raise = False
        self.score_debug = ''


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_card_image(self):
        return f'images/decks/{self.suit}/{self.value}.gif'


class Player:
    def __init__(self, name, avatar, cards, is_player: bool = True, is_opponent: bool = False, is_bot: bool = False):
        self.name = name
        self.avatar = avatar
        self._is_button = False
        self._badge = None
        self.is_player = is_player
        self.is_opponent = is_opponent
        self.is_bot = is_bot
        self.cards_in_hand = deepcopy(cards)
        self.game_data = GameData()
        self.round_data = RoundData()

    def update_badge(self, badge):
        badge.set_name(self.name)
        badge.set_avatar(self.avatar)
        badge.set_status(f'{"Your turn" if self.is_player else ("Bot " if self.is_bot else "") + self.name + " turn"}')
        badge.render()

    def set_type(self, is_player: bool = False, is_opponent: bool = False, is_bot: bool = False):
        self.is_player = is_player
        self.is_opponent = is_opponent
        self.is_bot = is_bot
        return self

    @property
    def is_button(self):
        return self._is_button

    @is_button.setter
    def is_button(self, is_button):
        self._is_button = is_button

    @property
    def badge(self):
        return self._badge

    @badge.setter
    def badge(self, badge):
        self._badge = badge

    def wait_for_play(self, callback):
        pass

    def reset_round_data(self):
        self.round_data = RoundData()

    def play_using_AI(self, board_cards, others):
        round_data = RoundData()
        current_score = get_player_score(board_cards + self.cards_in_hand)
        if current_score[0] > 1:
            round_data.bet = max([other.round_data.bet for other in others])
            round_data.score_debug = ' '.join([str(value) for value in current_score])
        return round_data
