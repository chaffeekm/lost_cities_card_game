# Project Name & Description
Lost Cities Card Game

A Python-based two-player card game based on the real card game, 'Lost Cities'. This is a pass'n'play game in which a player takes their own turn and then passes to the next player.

OFFICIAL GAME DESCRIPTION: "Lost Cities is a two-player card game where you embark on expeditions to five ancient lost cities. Players strategically play cards to build ascending sequences in their expeditions, aiming to score points while managing the risk of failed ventures."

OFFICIAL GAME INSTRUCTIONS:
"Starting the Game: The oldest player goes first.
Playing a Card: On your turn, you must first play a card from your hand:
Start a New Expedition: Place a card in a new column on your side of the board. This initiates an expedition to that color’s lost city.
Extend an Existing Expedition: Add a card to a column you’ve already started. The new card MUST have a higher value than the previously played card in that column.
Discard a Card: If you can’t or don’t want to play a card to an expedition, discard it face-up onto the corresponding color’s discard pile on the game board.
Drawing a Card: After playing a card, draw a new card from either:
The face-down draw pile.
The top of any of the five face-up discard piles.
Important: You cannot draw the card you just discarded.
Opponent’s Turn: The other player now takes their turn, following the same steps.

Scoring
Game End: The game ends immediately when a player draws the last card from the draw pile.
Calculating Scores: Each player calculates their score for each completed expedition (columns of cards):
Sum the Cards: Add up the face values of all the cards in the expedition column.
Expedition Cost: Subtract 20 points for the cost of funding the expedition.
Wager Multiplier: If you played any wager cards at the start of the expedition, multiply the result:
1 wager card: Multiply by 2
2 wager cards: Multiply by 3
3 wager cards: Multiply by 4
8+ Card Bonus: If the expedition column has 8 or more cards, add a 20-point bonus.
Total Score: Add up the scores from all five expeditions. The player with the highest total score wins.

Important Notes
Negative Scores: It’s possible to have negative scores for an expedition if the card values don’t outweigh the 20-point expedition cost.
Ascending Order: Cards in an expedition column MUST be placed in ascending order (2, 3, 4…).
Wager Cards: Wager cards can only be played at the BEGINNING of an expedition column, before any numbered cards."

## Features

* Displays the card game using the turtle module
* Receives input from the users to determine what action they want to take on their turn
* Randomly shuffles and keeps track of the deck
* Determines when the game is over (when the deck is empty) and which player scored the most points

## Technologies

* Python
* Turtle

## How It Works
* The card game is displayed using the turtle module
* Players take turns deciding what action they want to take, and then passing to the next player
* The app determines whether the player's choice for action is legal or not, and will ensure only legal moves can be made
* The app determines when the deck is empty, and then scores the game and determines the winner.

