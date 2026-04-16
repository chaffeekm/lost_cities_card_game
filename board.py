from card import Card, CARD_HEIGHT
from random import shuffle


# below constants can be changed if desired
CARD_COLORS = ["red", "green", "blue", "white", "yellow"]
CARD_NUMBERS = ["x", "+", "*", 2, 3, 4, 5, 6, 7, 8, 9, 10]
LOST_CITIES_CARDS = []
for color_type in CARD_COLORS:
    for number_type in CARD_NUMBERS:
        LOST_CITIES_CARDS.append((color_type, number_type))
shuffle(LOST_CITIES_CARDS)

# below constants will change automatically according to the above constants and constants from card
DISTANCE_BETWEEN_CARDS = CARD_HEIGHT * 30
DECK_PLACEMENT = DISTANCE_BETWEEN_CARDS * -3 - 20
CARD_PLACEMENT = []
card_location = DECK_PLACEMENT + DISTANCE_BETWEEN_CARDS + 20
for color_type in CARD_COLORS:
    CARD_PLACEMENT.append(card_location)
    card_location += DISTANCE_BETWEEN_CARDS


class Board:

    def __init__(self):
        self.total_cards = len(LOST_CITIES_CARDS)
        self.current_board = {} # card colors as keys, list of card numbers (discarded on board) as values
        self.card_objects = {} # card colors as keys, card objects (turtles) as values
        self.deck = Card("grey", f"Cards: {self.total_cards}") # deck object (turtle)
        self.setup()

    # EXAMPLE: self.current_board = {"red": [4, 3, 5], "green": [], "blue": [2, 6], "white": [2], "yellow": [7]}
    def setup(self):
        first_color = Card(CARD_COLORS[0], "-")
        first_color.move_card(CARD_PLACEMENT[0], 0, "board", "user")
        self.current_board[CARD_COLORS[0]] = []
        self.card_objects[CARD_COLORS[0]] = first_color
        self.deck.move_card(DECK_PLACEMENT, 0, "board", "user")
        for color_index in range(1, len(CARD_COLORS)):
            color_on_board = Card(CARD_COLORS[color_index], "-")
            color_on_board.move_card(CARD_PLACEMENT[color_index], 0, "board", "user")
            self.current_board[CARD_COLORS[color_index]] = []
            self.card_objects[CARD_COLORS[color_index]] = color_on_board

    def refresh_board(self):
        color_index = 0
        for color in self.current_board:
            if self.current_board[color]:
                top_card = self.current_board[color][-1]
            else:
                top_card = "-"
            self.card_objects[color].label_card(top_card, CARD_PLACEMENT[color_index], CARD_HEIGHT * 15, "board", "user")
            color_index += 1

    def add_to_board(self, color, number):
        self.current_board[color].append(number)
        self.refresh_board()

    def take_from_board(self, color):
        number = self.current_board[color][-1]
        del self.current_board[color][-1]
        self.refresh_board()
        return number

    def draw_card(self):
        self.total_cards -= 1
        self.deck.label_card(f"Cards: {self.total_cards}", DECK_PLACEMENT, CARD_HEIGHT * 16, "board", "user")

