from turtle import Screen
from card import WIDTH, HEIGHT
from board import Board, LOST_CITIES_CARDS
from field import Field
from hand import Hand
from input import custom_exact_input

dialogue_box = (int(round(WIDTH * 0.75, 0)), int(round(WIDTH * 0.089, 0)))
switch_players_dialogue_box = (int(round(WIDTH * 0.75, 0)), int(round(WIDTH * 0.74, 0)))

screen = Screen()
screen.title("Lost Cities")
screen.tracer(0)
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("NavajoWhite4")
root = screen._root


user_hand = Hand("user")
comp_hand = Hand("computer")
board = Board()
user_field = Field()
comp_field = Field()


def playable_cards(player_field, player_hand):
    cards_in_field = player_field.current_cards # Dictionary with colors as keys and list of numbers as values
    cards_in_hand = player_hand.current_hand # List of tuples (color, number)
    last_played_colors = {}
    playable_cards_in_hand = []
    for color in cards_in_field:
        if cards_in_field[color]:
            last_played_color = cards_in_field[color][-1]
            if last_played_color in ["x", "*", "+"]:
                last_played_color = 1
        else:
            last_played_color = 0
        last_played_colors[color] = last_played_color # {'red': 2, 'blue': '0', 'green': 5}
    for card in cards_in_hand:
        color = card[0]
        number = card[1]
        if number in ["x", "*", "+"]:
            number = 1
        if last_played_colors[color] in [0, 1]:
            playable_cards_in_hand.append(card)
        elif number == 1 and last_played_colors[color] != 1:
            pass
        elif number > last_played_colors[color]:
            playable_cards_in_hand.append(card)
    return playable_cards_in_hand


def colors_available_to_draw(current_board):
    cards_on_board = current_board.current_board # Dictionary with colors as keys and list of numbers as values
    colors_available = []
    for color in cards_on_board:
        if cards_on_board[color]:
            colors_available.append(color)
    return colors_available


def player_turn(current_board, player_field, player_hand, player_name):
    playable_cards_in_hand = playable_cards(player_field, player_hand)
    playable_colors = []
    for card in playable_cards_in_hand:
        playable_colors.append(card[0])
    # Takes user input for their turn action
    discard_or_play = custom_exact_input("", f"{player_name}, would you like to play or discard?", dialogue_box[0]-15, dialogue_box[1], root).lower()
    number = ""
    while discard_or_play not in ["discard", "play"]:
        discard_or_play = custom_exact_input("", "Invalid entry. Please try again.\nWould you like to play or discard?", dialogue_box[0]-15, dialogue_box[1], root).lower()
    color = custom_exact_input("", "What is the color of the card you would like to use?", dialogue_box[0]-49, dialogue_box[1], root).lower()
    # User chooses a card to play
    if discard_or_play == "play":
        while color not in playable_colors:
            color = custom_exact_input("", "Invalid entry. Please try again.\nWhat is the color of the card you would like to use?", dialogue_box[0]-40, dialogue_box[1], root).lower()
        number = custom_exact_input("", "What is the number of the card you would like to use?\nType x, +, or * accordingly if it is a multiplier.", dialogue_box[0]-57, dialogue_box[1], root).lower()
        if number not in ["x", "+", "*", ""]:
            number = int(number)
        playable_numbers = []
        for card in playable_cards_in_hand:
            if card[0] == color:
                playable_numbers.append(card[1])
        while number not in playable_numbers:
            number = custom_exact_input("","Invalid entry. Please try again.\nWhat is the number of the card you would like to use?\nType x, +, or * accordingly if it is a multiplier.", dialogue_box[0]-57, dialogue_box[1], root).lower()
            if number not in ["x", "+", "*", ""]:
                number = int(number)
        player_field.play_card(color, number)
    # User chooses a card to discard
    elif discard_or_play == "discard":
        colors_in_hand = []
        for card in player_hand.current_hand:
            colors_in_hand.append(card[0])
        while color not in colors_in_hand:
            custom_exact_input("", "Invalid entry. Please try again.\nWhat is the color of the card you would like to use?", dialogue_box[0]-40, dialogue_box[1], root).lower()
        number = custom_exact_input("", "What is the number of the card you would like to use?\nType x, +, or * accordingly if it is a multiplier.", dialogue_box[0]-57, dialogue_box[1], root).lower()
        if number not in ["x", "+", "*", ""]:
            number = int(number)
        playable_numbers = []
        for card in player_hand.current_hand:
            if card[0] == color:
                playable_numbers.append(card[1])
        while number not in playable_numbers:
            number = custom_exact_input("", "Invalid entry. Please try again.\nWhat is the number of the card you would like to use?\nType x, +, or * accordingly if it is a multiplier.", dialogue_box[0]-57, dialogue_box[1], root).lower()
            if number not in ["x", "+", "*", ""]:
                number = int(number)
        current_board.add_to_board(color, number)
    player_hand.remove_from_hand(color, number)
    # Takes user input for their draw
    screen.update()
    deck_or_board = custom_exact_input("", "Would you like to draw from the deck or the board?", dialogue_box[0]-50, dialogue_box[1], root).lower()
    board_empty = True
    for color in current_board.current_board:
        if current_board.current_board[color]:
            board_empty = False
    while deck_or_board not in ["deck", "board"] or (deck_or_board == "board" and board_empty):
        deck_or_board = custom_exact_input("", "Invalid entry. Please try again.\nWould you like to draw from the deck or the board?", dialogue_box[0]-50, dialogue_box[1], root).lower()
    # User draws from the deck
    if deck_or_board == "deck":
        current_board.draw_card()
        drawn_card = LOST_CITIES_CARDS[0]
        drawn_card_color = drawn_card[0]
        drawn_card_number = drawn_card[1]
        player_hand.add_to_hand(drawn_card_color, drawn_card_number, "user")
        del LOST_CITIES_CARDS[0]
    # User draws from the board
    elif deck_or_board == "board":
        colors_available = colors_available_to_draw(current_board)
        color = custom_exact_input("", "What is the color of the card you would like to take?", dialogue_box[0]-45, dialogue_box[1], root).lower()
        while color not in colors_available:
            color = custom_exact_input("", "Invalid entry. Please try again.\nWhat is the color of the card you would like to take?", dialogue_box[0]-45,dialogue_box[1], root).lower()
        number = current_board.take_from_board(color)
        player_hand.add_to_hand(color, number, "user")
    screen.update()


# {"red": ['x2', 4, 3, 5], "green": [], "blue": [2, 6], "white": [2], "yellow": [7]}
def score(player_field):
    total_score = 0
    field_cards = player_field.current_cards
    for color in list(field_cards):
        cards_of_color = field_cards[color]
        if cards_of_color:
            points_earned = 0
            multiplier = 1
            for card_number in cards_of_color:
                if card_number in ["x", "+", "*"]:
                    multiplier += 1
                else:
                    points_earned += card_number
            points_gained = points_earned - 20
            total_score += points_gained * multiplier
    return total_score


game_on = True
player = 2
screen.update()
who_is_playing = custom_exact_input("", f"Welcome to 'Lost Cities'! Who will be playing? Type both names, separated by a comma.",switch_players_dialogue_box[0] - 150, switch_players_dialogue_box[1],root).title()
player_names = who_is_playing.split(",")
for i in range(len(player_names)):
    player_names[i] = player_names[i].strip()
player_1 = player_names[0]
player_2 = player_names[1]
while game_on:

    # Active player takes turn
    screen.update()
    if player % 2 == 0:
        pass_to_player = player_2
        player_turn(board, user_field, user_hand, player_1)
    else:
        pass_to_player = player_1
        player_turn(board, comp_field, comp_hand, player_2)
    user_hand.clear_hand()
    comp_hand.clear_hand()

    # Determines if game is over, calculates scores, and determines winner
    if board.total_cards == 0:
        game_on = False
        user_score = score(user_field)
        comp_score = score(comp_field)
        if comp_score > user_score:
            custom_exact_input("", f"{player_2} wins with a score of {comp_score}!\n{player_1} got a score of {user_score}.", dialogue_box[0] - 10, dialogue_box[1], root)
        elif comp_score < user_score:
            custom_exact_input("", f"{player_1} wins with a score of {user_score}!\n{player_2} got a score of {comp_score}.", dialogue_box[0] - 10, dialogue_box[1], root)
        else:
            custom_exact_input("", f"Players tied with a score of {user_score}!", dialogue_box[0] - 10, dialogue_box[1], root)

    # Switches board around for new active player (if game not over)
    elif player % 2 == 0:
        custom_exact_input("", f"                              Pass to {pass_to_player}. Then when {pass_to_player} is ready, hit enter.                              ", switch_players_dialogue_box[0] - 135, switch_players_dialogue_box[1], root).lower()
        user_hand.setup("computer", user_hand.current_hand)
        comp_hand.setup("user", comp_hand.current_hand)
        user_field.switch_field("computer")
        comp_field.switch_field("user")
    else:
        custom_exact_input("", f"                              Pass to {pass_to_player}. Then when {pass_to_player} is ready, hit enter.                              ", switch_players_dialogue_box[0] - 135, switch_players_dialogue_box[1], root).lower()
        user_hand.setup("user", user_hand.current_hand)
        comp_hand.setup("computer", comp_hand.current_hand)
        user_field.switch_field("user")
        comp_field.switch_field("computer")
    player += 1


screen.exitonclick()

