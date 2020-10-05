import kivy
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label

from copy import deepcopy
from typing import Callable
from random import shuffle, choice

from games.constants import SUITS, AVATARS
from games.controls.board_cards_render import BoardCardsRender
from games.controls.player_badge import TurtlePlayerBadgeControl
from games.entities import Card, Player
from games.pocker_utils import splice
from games.screen import Screen


class Game(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bank = 0
        self.round = 0
        self.deck = []
        self.players = []
        self._board_cards = []
        self.current_player = 0
        self.__players_play_queue = None
        self.__board_render = None
        self.__random_avatars = []

    @staticmethod
    def _make_deck():
        deck = []
        for suit in SUITS:
            deck.extend([Card(value, suit) for value in range(2, 15)])
        shuffle(deck)
        return deck

    def play_round(self):
        self.next_player_plays()

    def next_player_plays(self):
        while self.current_player + 1 != len(self.__players_play_queue):
            player = self.__players_play_queue[self.current_player]
            self.__players_play_queue[self.current_player].badge.activate()
            print(f'{player.name}{" (bot)" if player.is_bot else ""} is playing')
            # player.update_badge(self.__player_badge)
            if player.is_bot:
                self.on_player_played(player.play_using_AI(self._board_cards,
                                                           filter(lambda item: item is not player, self.players)))
            elif player.is_player:
                player.wait_for_play(lambda data: self.on_player_played(data))
            elif player.is_opponent:
                # todo Write remote play support
                pass
            break
        else:
            self.on_round_played()

    def on_round_played(self):
        pass

    def on_player_played(self, new_round_data):
        self.__players_play_queue[self.current_player].round_data = new_round_data
        self.__players_play_queue[self.current_player].badge.set_bet(new_round_data.bet)
        self.__players_play_queue[self.current_player].badge.set_status(new_round_data.score_debug)
        self.__players_play_queue[self.current_player].badge.deactivate()
        self.current_player += 1
        self.next_player_plays()

    def prepare(self):
        self.bank = 0
        self.round = 0
        self.deck = self._make_deck()
        self.__random_avatars = deepcopy([*AVATARS.items()])

    def __get_initial_board_cards(self):
        return splice(self.deck, 0, 3)

    def __create_random(self):
        if len(self.__random_avatars) > 0:
            player = choice(self.__random_avatars)
            self.__random_avatars.remove(player)
        else:
            return None
        name, avatar = player
        return Player(name, avatar, splice(self.deck, 0, 2))

    def __next_random_player(self):
        while True:
            random_player = self.__create_random()
            if random_player:
                yield random_player
            else:
                break

    def __create_badges(self):
        self.__player_badges = []
        canvas = Screen.get_canvas()
        top, right, bottom, left = [
            [self.players[-1], self.players[0]],
            self.players[1:4],
            self.players[4:6],
            self.players[6:-1]
        ]
        for y, players in {5: top, canvas.winfo_height() - 205: bottom}.items():
            x = canvas.winfo_width() / 2 - 310
            for idx, player in enumerate(players):
                if idx > 0:
                    x += 10
                player.badge = TurtlePlayerBadgeControl(x=x, y=y)
                player.badge.set_name(player.name)
                player.badge.set_avatar(player.avatar)
                player.badge.set_bet(player.round_data.bet)
                player.badge.set_cards(player.cards_in_hand)
                x += 310
        for x, players in {5: left, canvas.winfo_width() - 315: right}.items():
            y = 105
            for idx, player in enumerate(players):
                if idx > 0:
                    y += 10
                player.badge = TurtlePlayerBadgeControl(x=x, y=y)
                player.badge.set_name(player.name)
                player.badge.set_avatar(player.avatar)
                player.badge.set_bet(player.round_data.bet)
                player.badge.set_cards(player.cards_in_hand)
                y += 200

    def build(self):
        main_layout = BoxLayout(orientation='vertical')
        top = AnchorLayout(anchor_x='center', anchor_y='top')
        stack = StackLayout(size_hint=(None, 0))
        stack.add_widget(Button(text='One', size_hint=(None, None)))
        stack.add_widget(Button(text='Two', size_hint=(None, None)))
        top.add_widget(stack)
        main_layout.add_widget(top)
        return main_layout

    def play(self):
        self.run()
        return
        self.prepare()
        self.players = [player.set_type(is_bot=True) for player in list(self.__next_random_player())]
        self.players[0].set_type(is_player=True)
        self.players[0].is_button = True
        self.players[1].round_data.bet = 1
        self.players[2].round_data.bet = 2
        self.__players_play_queue = [self.players[3], *self.players[4:], *self.players[0:3]]
        self.current_player = 0
        self.__create_badges()
        self.__board_render = BoardCardsRender()
        self._board_cards = self.__get_initial_board_cards()
        self.__board_render.push_card(*self._board_cards)
        self.__board_render.render()
        self.play_round()

