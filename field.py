from board import CARD_COLORS, CARD_PLACEMENT
from card import Card, CARD_WIDTH


USER_DISTANCE_FROM_BOARD = CARD_WIDTH * -20
COMP_DISTANCE_FROM_BOARD = CARD_WIDTH * 21
DISTANCE_BETWEEN_CARDS_Y = CARD_WIDTH + 10

USER_CARD_PLACEMENT = []
card_shift = USER_DISTANCE_FROM_BOARD
for possible_card in range(13):
    USER_CARD_PLACEMENT.append(card_shift)
    card_shift -= DISTANCE_BETWEEN_CARDS_Y

COMP_CARD_PLACEMENT = []
card_shift = COMP_DISTANCE_FROM_BOARD
for possible_card in range(13):
    COMP_CARD_PLACEMENT.append(card_shift)
    card_shift += DISTANCE_BETWEEN_CARDS_Y


class Field:

    def __init__(self):
        self.current_cards = {} # card colors as keys, list of card numbers (played in front of board) as values
        self.card_objects = {}
        self.setup()

    def setup(self):
        for color in CARD_COLORS:
            self.current_cards[color] = []

    def play_card(self, color, number):
        card_info = (color, number)
        self.current_cards[color].append(number)
        card = Card(color, number)
        self.card_objects[card_info] = card
        color_index = CARD_COLORS.index(color)
        played_card_placement = len(self.current_cards[color])
        card.move_card(CARD_PLACEMENT[color_index], USER_CARD_PLACEMENT[played_card_placement], "card",
                       "user")

    def switch_field(self, user_or_computer):
        passive_card_objects = {}
        passive_current_cards = {}
        for color in CARD_COLORS:
            passive_current_cards[color] = []
        for card_object in list(self.card_objects):
            card = self.card_objects[card_object]
            color = card_object[0]
            number = card_object[1]
            card_info = (color, number)
            passive_current_cards[color].append(number)
            played_card_placement = len(passive_current_cards[color])
            color_index = CARD_COLORS.index(color)
            card.remove_card()
            new_card = Card(color, number)
            passive_card_objects[card_info] = new_card
            if user_or_computer == "user":
                new_card.move_card(CARD_PLACEMENT[color_index], USER_CARD_PLACEMENT[played_card_placement], "card",
                               user_or_computer)
            else:
                new_card.move_card(CARD_PLACEMENT[color_index], COMP_CARD_PLACEMENT[played_card_placement], "card",
                               user_or_computer)
        self.card_objects = passive_card_objects

