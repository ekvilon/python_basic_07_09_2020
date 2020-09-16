from random import shuffle
import turtle

card_jack_value = 11
card_queen_value = 12
card_king_value = 13
card_ace_value = 14

suit_spades = '♠'
suit_hearts = '♥'
suit_clubs = '♣'
suit_diamonds = '♦'


def splice(items, start, count):
    return list(items.pop(start) for _ in range(0, count))


def card(value, suit):
    return {
        value,
        suit
    }


def make_deck():
    suits = (suit_spades, suit_hearts, suit_clubs, suit_diamonds)
    deck = []
    for suit in suits:
        deck.extend(card(value, suit) for value in range(2, card_ace_value + 1))
    shuffle(deck)
    return deck


def render_table(cards_on_table):
    turtle.bgpic('pocker_bg.gif')
    turtle.bgcolor('black')
    for idx, card in enumerate(cards_on_table):
        piece = turtle.Turtle()
        offset = idx * 100 + 10
        shape = turtle.Shape('compound')
        poly1 = ((100, offset), (100, offset + 75), (0, offset + 75), (0, offset))
        shape.addcomponent(poly1, 'white', 'black')
        turtle.register_shape(f'table_card_{idx}', shape)
        piece.shape(f'table_card_{idx}')

def debug(x, y):
    print(x, y)


def play():
    game = {
        'round': 0,
        'cards_on_table': []
    }
    player = {
        'name': '',
        'cards_in_hand': [],
        'is_passing': False,
        'score': 0
    }
    bot = {
        'name': 'Jeeves',
        'cards_in_hand': [],
        'is_passing': False,
        'score': 0
    }
    deck = make_deck()
    game['cards_on_table'] = splice(deck, 0, 3)
    render_table(game['cards_on_table'])
    turtle.onscreenclick(debug)
    turtle.mainloop()


if __name__ == '__main__':
    play()