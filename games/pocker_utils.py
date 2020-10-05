from games.constants import SUITS


def splice(items, start, count):
    return list(items.pop(start) for _ in range(0, count))


def get_player_score(cards):
    all_sorted_cards = sorted(cards, key=lambda sorted_card: sorted_card.value)
    all_cards_values = list(map(lambda sorted_card: sorted_card.value, all_sorted_cards))

    # checking on street-flash
    street_flash = None
    for suit in SUITS:
        cards_from_same_suite = [card for card in all_sorted_cards if card.suit == suit]
        if len(cards_from_same_suite) > 4:
            for num in range(0, 3):
                full_set = [test_card for idx, test_card in enumerate(cards_from_same_suite[num:], num)
                            if idx == num or test_card.value == cards_from_same_suite[idx - 1].value + 1][:5]
                if len(full_set) == 5:
                    street_flash = (9, full_set[0].value)
    if street_flash:
        return street_flash

    # checking on square
    for square_card_value in sorted(frozenset(all_cards_values), reverse=True):
        if all_cards_values.count(square_card_value) == 4:
            return tuple([8, square_card_value] +
                         max([card_value for card_value in all_cards_values if card_value != square_card_value]))

    # checking on full-house
    card_occurrences = {}
    for full_house_card_value in frozenset(all_cards_values):
        card_occurrences[full_house_card_value] = all_cards_values.count(full_house_card_value)
    three_card_packs = [card_value for card_value, occurrences in card_occurrences.items() if occurrences == 3]
    two_card_packs = [card_value for card_value, occurrences in card_occurrences.items() if occurrences == 2]
    if len(three_card_packs) and (len(three_card_packs) == 2 or len(two_card_packs)):
        return 7, max(three_card_packs)

    # checking on flash
    for suit in SUITS:
        cards_from_same_suite = [card for card in all_sorted_cards if card.suit == suit]
        if len(cards_from_same_suite) > 4:
            return tuple([6] + [card.value for card in cards_from_same_suite[-5:]])

    # checking on street
    street = 0
    for num in range(0, 3):
        start_value = all_cards_values[num]
        matches = False
        if not num or (num and num + 5 <= len(all_cards_values)):
            for idx, test_value in enumerate(range(start_value, start_value + 5), num):
                matches = all_cards_values[idx] == test_value
                if not matches:
                    break
        if matches:
            street = (5, start_value)
    if street:
        return street

    # checking on thrips
    for candidate in frozenset(all_cards_values):
        if all_cards_values.count(candidate) == 3:
            return tuple([4, candidate] +
                         [card_value for card_value in all_cards_values[-1::-1]
                          if card_value != candidate])

    # checking on two pairs
    pair_values = [card_value for card_value in frozenset(all_cards_values[-1::-1])
                   if all_cards_values.count(card_value) == 2][:2]
    if len(pair_values) > 1:
        return tuple([3, pair_values[0], pair_values[1]] + [value for value in all_cards_values[-1::-1]
                                                            if value not in pair_values])

    # checking on one pair
    pair_value = [card_value for card_value in sorted(frozenset(all_cards_values), reverse=True)
                  if all_cards_values.count(card_value) == 2][:1]
    if pair_value:
        return tuple([2, pair_value[0]] + [value for value in all_cards_values[-1::-1]
                                           if value != pair_value[0]])

    # higher card
    return tuple([1] + all_cards_values[-1::-1])


def players_has_greater_score(first, second):
    for n, score in enumerate(first['game_data']['score']):
        if score > second['game_data']['score'][n]:
            return True
        else:
            return False
    return False


def players_has_same_score(first, second):
    return frozenset(first['game_data']['score']) == frozenset(second['game_data']['score'])


def get_winners(players):
    if not players:
        return []

    player = players[0]
    better = get_winners([better for better in players if better != player and
                          players_has_greater_score(better, player)])
    same = [same for same in players if same != player and players_has_same_score(same, player)]

    return better if better else ([player] + same)
