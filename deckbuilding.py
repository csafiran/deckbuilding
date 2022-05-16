import math
import random
from tkinter import Menu

from matplotlib.pyplot import draw

#from pyrsistent import discard

#####
# User Interface
#####

class BoardState:
    def __init__(self):
        self.points = 60
        self.monster_cards = [None for i in range(6)]
        self.center_cards = [None for i in range(6)]
        for i in range(6):
            self.renew_card(i)
        for i in range(6):
            self.renew_monster(i)
    
    def renew_card(self,index):
        #switch from uniform probability
        new_card1 = random.choices(range(1, 10),weights=[3,3,4,5,5,2,2,1,1])
        #add new_card to the list
        self.center_cards[index] = new_card1
        print(new_card1)
        return new_card1
        
    def renew_monster(self, index):
        #switch from uniform probability
        new_card2 = random.choices(range(1, 10),weights=[3,3,4,5,5,2,2,1,1])
        #add new_card to the list
        self.monster_cards[index] = new_card2
        return new_card2
   
    def __str__(self):
        # Display both card rows
        print(self.monster_cards)
        print(self.center_cards)
        
        # Display current point pool level
        return f" Points remaining: '{self.points}'"

#####
# Game Logic
#####

def remove_choice(population, k):
    # function for selecting removing selected card
    choice = []
    for i in range(k):
        choice.append(population.pop(random.randrange(len(population))))
    return choice


class Player:
    """Class for a deckbuilding player.
    
    Attributes:
        name (str): the player's name.
        money(int): the players money)
    """
    def __init__(self, name, path):
        self.name = name
        self.points = 0
        self.path = path
        self.draw_pile = []
        self.discard_pile = []
    
    def turn(self, state):
        """Take a turn. Draing the player's hand and having the player make 
        decisions with their hand.
        
        Args:
            state (GameState): a snapshot of the current state of the game.
            
        Side Effects:
            May print gamestate or other UI information
        """
        hand = self.draw()
        
        # calculate total money availble
        money = sum([card.money_payout for card in hand])

        # calculate total kombat available
        combat = sum([card.combat_payout for card in hand])

        # display state
        print(f"Board: {state}")
        print("Hand:")
        for card in hand:
            print(f"* {card}")

        # UI
        cont = True
        while cont:
            print(f"Remaining Money: {money}")
            print(f"Remaining Combat: {combat}")
            print("please type 1:for spend money to buy card")
            print("2: for attack monster")
            choice = input(f"What to do? ??")
            if choice == 1:
                mc = input("please choose which card do you want to buy")
                money -= BoardState.center_cards[mc]
                hand += BoardState.center_cards[mc]
                print(f"now you have {money} left")
                break
            if choice == 2:
                km = input("please choose which monster do you want to kill")
                combat -= BoardState.monster_cards[km]
                self.points += BoardState.monster_cards[km] + 1
                print(f"now you get{BoardState.monster_cards[km] + 1} points")
                break


            # TODO stub
            cont = False

        # discard hand at end of turn
        self.discard_pile.extend(hand)

        # print(GameState)
        # print(self.name + "'s hand: " + str(hand))
        
    def draw(self):
        """
        function to draw five cards from the player's deck. Returns "cards" as
        a list. Adds them to the player's discard pile. This function will 
        automatically take cards from the player's discard pile when the deck
        has zero cards and still needs to draw one or more.
        """

        # load deck from file
        deck = []
        with open(self.path, encoding="UTF-8") as f:
            for line in f:
                line = line.strip()  # remove leading and trailing whitespace
                if len(line) > 0:    # ignore blank lines
                    deck.append(Card(line))

        # draw 5 cards or remaining deck, which ever is smaller
        hand = remove_choice(deck, min(5, len(deck)))

        # check if we have 5 cards
        if len(hand) < 5:
            # if not, discard pile becomes deck
            deck = self.discard_pile
            self.discard_pile = []

            # draw remaining cards (Note: not handling case where there are less then 5 cards between deck and discard)
            hand.extend(remove_choice(deck, 5 - len(hand)))
        
        # save deck to file
        with open(self.path, "w", encoding="UTF-8") as f:
            for card in deck:
                f.write(f"{repr(card)}\n")
        
        return hand
                            
    def calc_score(self,player):
        return player.points 

            #if player1 > player2:
            #    print("player1 win!!")
                
            #elif player2 > player1:
            #    print("player2 win!!")
            #else:
            #    print("It is a tie")
                
            
    # TODO Stubby

class Card:
    def __init__(self, card_string):
        print(f"Card.__init__({card_string}") #for debugging
        
        #creating an iterator for parsing
        self.card_string = card_string
        fields = card_string.split(",")
        
        #assigning each attribute in the card with an index  
        self.name = fields[0]
        self.card_type = fields[1]
        self.cost = int(fields[2])
        self.money_payout = int(fields[3])
        self.combat_payout = int(fields[4])
    
    def __str__(self):
        return f'{self.name}: {max(self.money_payout, self.combat_payout)}'
    
    def __repr__(self):
        return self.card_string
        
    
    def defeat(self, player, whichm):
        """function that will represent what happens when a player defeats a monster 
    card from the center row
        """
        if whichm <= 0:
            player.points += whichm + 1

    def action(self):
        """function that will represent the actions the player does with their cards
        in their hand   
        """





        
        
def test1():
    
    player117 = Player("John", "player1Deck.txt")
    package  = Player("Cortana", "player2Deck.txt")

    while 1 == 1:
        print("starttest1")
        print(player117.name)
        print(player117.draw()) 
        print(package.name)
        print(package.draw())   
        print("endtest1")   

def test2():
    #switch from uniform probability
    #if self.center_cards < 5:
    new_card = random.choices(range(1, 10),weights=[3,3,4,5,5,2,2,1,1])
        #add new_card to the list
        #self.center_cards[i] = new_card
    print(new_card)
    #return new_card

def main():
    """
    The main function is mainly used to call other functions and run our game.

    return:
    it will return the state of the game

    Side Facts:
    it will print the info of the game.
    """
    #Main menu: We need two player names
    p1name = "John"
    p2name = "Cortana"
    
    #Construct the GameState
    board = BoardState()
    players = [Player(p1name, "player1Deck.txt"), Player(p2name, "player2Deck.txt")]
    turn = 0
    
    #Gameloop - Alternate player1 and player2 turn until game is over
    while turn != 0 or board.points > 0:
        players[turn].turn(board)
        turn = (turn + 1) % len(players)
    
    #Declare winner (cleanup: reset temp files)
    max_score = -1
    winners = []
    for player in players:
        score = Player.calc_score(player)
        if score > max_score:
            winners = [player]
        elif score == max_score:
            winners.append(player)
    print("Winner(s): " + str(winners))
    # TODO: Clean up??

if __name__ == "__main__":
    #test1()
    #test2()
    #BoardState()
    #print(Player("Cyrus", "player1Deck.txt").draw())
    main()
