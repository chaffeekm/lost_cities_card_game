from turtle import Turtle


# below constants can be changed if desired
FONT = ("Courier", 9, "normal")
WIDTH = 900

# below constants will change automatically according to the above constants
HEIGHT = WIDTH // 1.28
CARD_WIDTH = WIDTH // 151
CARD_HEIGHT = HEIGHT // 176


class Card(Turtle):

    def __init__(self, color, number):
        super().__init__()
        self.hideturtle()
        self.color = color
        self.number = number
        self.card_object = []
        self.card_label_object = []
        self.create_card(color)
        self.label_card(number, CARD_WIDTH - 6, CARD_HEIGHT * 15, "board", "user")

    def create_card(self, color):
        new_card = Turtle("square")
        new_card.penup()
        new_card.color(color)
        new_card.pencolor("black")
        new_card.shapesize(stretch_len=CARD_HEIGHT, stretch_wid=CARD_WIDTH)
        self.card_object.append(new_card)

    def label_card(self, label, x, y, card_or_board, user_or_computer):
        if self.card_label_object:
            self.card_label_object[0].clear()
        self.card_label_object = []
        new_card_number = Turtle()
        new_card_number.hideturtle()
        new_card_number.penup()
        if card_or_board == "card":
            if user_or_computer == "user":
                new_card_number.goto(x - 38, y - (CARD_WIDTH * -7))
            else:
                new_card_number.goto(x - 38, y - (CARD_WIDTH * 10))
        elif card_or_board == "board":
            new_card_number.goto(x, CARD_HEIGHT * 17)
        else:
            new_card_number.goto(x - 10, y + (CARD_WIDTH * 10))
        new_card_number.write(label, align="center", font=FONT)
        self.card_label_object.append(new_card_number)

    def move_card(self, x, y, card_or_board, user_or_computer):
        self.card_object[0].goto(x, y)
        self.label_card(self.number, CARD_WIDTH + x - 6, y, card_or_board, user_or_computer)

    def remove_card(self):
        self.card_label_object[0].clear()
        self.card_object[0].hideturtle()

