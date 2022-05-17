# Team 23's Deckbuilding game
For INST326 deckbuilding project
deckbuilding.py - The python file that contains the deckbuilding game
player1Deck - The text file that holds player 1's cards
player2Deck - The text file that holds player 2's cards

To run:
Enter "deckbuilding.py" into the command line
Afterward, follow prompts in the terminal

How to play:
The goal of the deckbuilding game is to get the most points.
There are a total of 60 points in the point pool.
You gain points by defeating monsters.
When navigating the menu, two rows will be displayed.
The top row are monster cards, which you defeated with combat.
Your reward would be 1 + the combat cost.
The bottom row are purchasable cards. When bought, these go into your discard to be draw again.
When your deck runs out of cards, you would shuffle your discard cards back into your deck.
The purchasable cards give money, combat points, or both.

How to read the card properly is as follows:
[card's name, M or P (monster or purchasable), int to represent the cost (monsters is combat cost and purchasable cards is money cost), money value, combat value]

The score is calculated at the end of the game. Enjoy!

Attribution: 
David: draw() and main()
He used with statements and conditionals

TMZ: Card Class()
He used f-strings and optional parameters and/or use of keyword arguments

Cyrus: The entire Boardstate Class() and turn()
He used magic methods and list comprehensions

