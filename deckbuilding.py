#importing math to use math.shuffle for the player's deck
import math
import random
from tkinter import Menu

#####
# User Interface
#####

#class Boardstate:          <--- commented out class (will be done later)


    # this is where the UI would go. We plan on doing this part last. It would most
    # likely be hardcoded at first.

#####
# Game Logicdddd
#####




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
        #player hand will be added to discard pile in gameState
        #discardPiple may also need to create a new text file that will 
        #be changed and replace deck text file once deck text file is empty
        self.drawPile = []
        self.discardPile = []
    #We may need to initilize our deck, handle, and discard piles here as well
    
    def turn(self, state):
        """Take a turn. Draing the player's hand and having the player make 
        decisions with their hand.
        
        Args:
            state (GameState): a snapshot of the current state of the game.
            
        Side Effects:
            May print gamestate or other UI information
        """
        hand = self.draw()
        money = addMoney(hand)
        kombat = addKombat(hand)
        chooseActions(self, state, money, kombat)
        #chooseActions will be used to include UI (display money, game state,
        # and kombat points)
        
        ##TODO:print(GameState)
    
    def draw(self):
        
        """
        function to draw five cards from the player's deck. Returns "cards" as
        a list. Adds them to the player's discard pile. This function will 
        automatically take cards from the player's discard pile when the deck
        has zero cards and still needs to draw one or more.
        """
        
        with open(self.path, encoding="UTF-8") as f:
            textList = []
            for line in f:
                line = line.strip()
                line = line.split()
                textList.append(line)
        #f.write line
        
        #playerDeck = np.array([textList])
        #handCards = [0]
        playerDeck = textList[0]
        playerHandDraw = []
        if len(playerDeck) >= 5:
            for char in len(textList):
                playerHandDraw+= playerDeck
                char +=1
        else:
            for char in len(textList):
                playerHandDraw += playerDeck
                char += 1
            playerDeck += self.discardPile
        return playerHandDraw
                
            
            
                
        random.shuffle(playerHandDraw)
        
        #TODO:if len(playerDeck) > 5:
            #TODO:self.playerDeck+= self.discard()   <------ MAY BE ADDED TO GAMESTATE
    
    
        return list(playerDeck[handCards])
    
    def buy(self, card):
        """Adds the card the player's discard pile

        Args:
            card (_type_): _description_
        """
        pass
    
class Monster:
    def __init__(self, hp, honer):
        self.hp = hp
        self.honer = honer




        


        
class GameAction:
    """
    """
    def __init__(self):
        """Set attributes."""


    
    def menu(self):
        while userResponse >= 1 & userResponse <=5:

            print(f"your have 5 card which is {Player.draw}")
            userResponse = input("which one would like you to use")
        return userResponse
    
    def battlecard(self):

        

    
    
        if userchoice == attack1:
            pass




    #function that will represent what happens when a player purchases a card
    #from the center row
    
    def defeat():
        """function that will represent what happens when a player defeats a monster 
    card from the center row
        """

    def action():
        """function that will represent the actions the player does with their cards
        in their hand   
        """
    def killed(self, pk, whichm):

        if whichm.hp <= 0:
            pk.honer += self.honer
        return f"Now you have {pk.honer} total honers"
        
def test1():
    print("starttest1")
    player117 = Player("John", "playerDeck.txt")
    print(player117.draw())    
    print("endtest1")   
        
def main():
    """
    The main function is mainly used to call other functions and run our game.

    return:
    it will return the state of the game

    Side Facts:
    it will print the info of the game.
    """
    m1 = Monster(random.randint(1,6), random.randint(1,5))
    m2 = Monster(random.randint(1,6), random.randint(1,5))
    m3 = Monster(random.randint(1,6), random.randint(1,5))
    m4 = Monster(random.randint(1,6), random.randint(1,5))
    m5 = Monster(random.randint(1,6), random.randint(1,5))
    monster5 = []
    player1 = Player("tmz")
    player2 = Player("sss")
    while True:
        us = GameAction.menu
        




    








if __name__ == "__main__":
    test1()
    #main()