from random import shuffle
from itertools import chain
from tkinter import PhotoImage
import turtle as Turtle
from turtle import Shape

card_joker_value = 0
card_jack_value = 11
card_queen_value = 12
card_king_value = 13
card_ace_value = 14

suit_spades = 'spades'
suit_hearts = 'hearts'
suit_clubs = 'clubs'
suit_diamonds = 'diamonds'


card_images = dict(chain({n: str(n) for n in range(2, 11)}.items(), {
    card_jack_value: 'jack',
    card_queen_value: 'queen',
    card_king_value: 'king',
    card_ace_value: 'ace',
    card_joker_value: 'joker'
}.items()))


def get_card_render():
    rendered_cards = dict({})

    def render_card(value, suit):
        key = f'card-{suit}-{value}'
        if not rendered_cards.get(key):
            image = PhotoImage(file=f'resources/images/decks/{suit}/{card_images[value]}.gif')
            Turtle.addshape(key, Shape('image', image))
            card = Turtle.Turtle()
            card.penup()
            card.left(90)
            card.shape(key)
            rendered_cards[key] = card, image.width(), image.height()
        return rendered_cards[key]

    return render_card


render_card = get_card_render()


def splice(items, start, count):
    return list(items.pop(start) for _ in range(0, count))


def card(value, suit):
    return {
        'value': value,
        'suit': suit
    }


def make_deck():
    suits = (suit_spades, suit_hearts, suit_clubs, suit_diamonds)
    deck = []
    for suit in suits:
        deck.extend(card(value, suit) for value in range(2, card_ace_value + 1))
    shuffle(deck)
    return deck


def render_table(game):
    Turtle.bgcolor('dark green')
    for idx, card in enumerate(game['cards_on_table']):
        value, suit = (card['value'], card['suit'])
        card['turtle'] = render_card(value, suit)


def debug(x, y):
    print(x, y)


def play():
    deck = make_deck()
    game = {
        'deck': deck,
        'cards_on_table': splice(deck, 0, 3),
        'player': {
            'name': '',
            'cards_in_hand': splice(deck, 0, 2),
            'is_passing': False,
            'score': 0
        },
        'bot': {
            'name': 'Jeeves',
            'cards_in_hand': splice(deck, 0, 2),
            'is_passing': False,
            'score': 0
        }
    }
    Turtle.onscreenclick(debug)
    Turtle.hideturtle()
    render_table(game)
    Turtle.mainloop()


if __name__ == '__main__':
    play()

