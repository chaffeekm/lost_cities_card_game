from board import CARD_COLORS, LOST_CITIES_CARDS, CARD_NUMBERS
from card import Card, HEIGHT, CARD_HEIGHT


DISTANCE_BETWEEN_CARDS = CARD_HEIGHT * 12

CARD_PLACEMENT = []
card_location = DISTANCE_BETWEEN_CARDS * -3.5
for card_spot in range(8):
    CARD_PLACEMENT.append(card_location)
    card_location += DISTANCE_BETWEEN_CARDS


class Hand:

    def __init__(self, user_or_computer):
        self.current_hand = [] # list of tuples with card color and card number
        self.card_objects = {} # dictionary with tuple of card as key, and turtle object as value
        self.user_or_computer = user_or_computer
        self.deal_hand()
        self.organize()
        self.setup(self.user_or_computer, self.current_hand)

    def deal_hand(self):
        for dealt_card in range(8):
            new_card = LOST_CITIES_CARDS[0]
            del LOST_CITIES_CARDS[0]
            self.current_hand.append(new_card)

    # [('blue', 8), ('blue', 6), ('yellow', 'x2'), ('blue', 'x2'), ('yellow', 9), ('blue', 'x2'), ('green', 'x2'), ('yellow', 5)]
    def organize(self):
        ordered_hand = []
        for color_order in CARD_COLORS:
            for number_order in CARD_NUMBERS:
                for dealt_card in self.current_hand:
                    if dealt_card[0] == color_order and dealt_card[1] == number_order:
                        ordered_hand.append(dealt_card)
        self.current_hand = ordered_hand

    def setup(self, user_or_computer, current_hand):
        for card_index in range(len(current_hand)):
            card = current_hand[card_index]
            if user_or_computer == "user":
                new_card = Card(card[0], card[1])
                self.card_objects[card] = new_card
                new_card.move_card(CARD_PLACEMENT[card_index], -HEIGHT // 2, "hand", "user")
            elif user_or_computer == "computer":
                new_card = Card("grey", "")
                self.card_objects[card] = new_card
                new_card.move_card(CARD_PLACEMENT[card_index], HEIGHT // 2, "hand", "computer")

    def clear_hand(self):
        for card_object in list(self.card_objects):
            color = card_object[0]
            number = card_object[1]
            card_to_remove = (color, number)
            self.card_objects[card_to_remove].remove_card()

    def remove_from_hand(self, color, number):
        card_to_remove = (color, number)
        self.card_objects[card_to_remove].remove_card()
        del self.card_objects[card_to_remove]
        index_of_card = self.current_hand.index(card_to_remove)
        del self.current_hand[index_of_card]

    def add_to_hand(self, color, number, user_or_computer):
        for card in list(self.card_objects):
            self.card_objects[card].remove_card()
        self.card_objects = {}
        card_to_add = (color, number)
        self.current_hand.append(card_to_add)
        self.organize()
        self.setup(user_or_computer, self.current_hand)

