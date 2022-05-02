#importing math to use math.shuffle for the player's deck
import math
import random

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
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.points = 0
        
        #player hand will be added to discard pile in gameState
        #discardPiple may also need to create a new text file that will 
        # be changed and replace deck text file once deck text file is empty
        
        self.discardPile = []
    #We may need to initilize our deck, handle, and discard piles here as well
    
    def turn(self, state):
        """Take a turn.
        
        Args:
            state (GameState): a snapshot of the current state of the game.
            
        Side Effects:
            May print gamestate 
        """
        
        
        ##TODO:print(GameState)
    
    def deck(self,path):
        
        """
        function to represent each player's deck of cards
        """
        
        with open(path, encoding="UTF-8") as f:
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
    
    
    def hand(self):
        """
        function to represent each player's hand of 5 cards
        """
        self.playerHand = []
        self.playerHand += (self.deck())
        return self.playerHand
    
class Monster:
    def __init__(self, hp, honer):
        self.hp = hp
        self.honer = honer
    def killed(self):
        if self.hp == 0:
            Player.honer += self.honer
        return f"Now you have {Player.honer} total honers"
        


        
class GameAction:
    """Provide information on the current state of the game. Used in the
    Player.turn() method.
    
    Attributes:
        board (str): a representation of the board, with cards represented as 
        list of strings.
        point_pool (int): the remaining points in the center row.
        center_cards (list of str): characters that represent a monster, 
        combat points, money, and a respective cost to defeat or aquire them 
        (in either combat points or money).
        center_deck (list of strings): a randomly generated assortment of cards
        that would enter the center row.
    """
    def __init__(self):
        """Set attributes."""
    def buy(self,money, item):
        """
        this function will do the calculation on the player's money, once this 
        function has been called, player will get something and money will be used
        
        Args:

        money:
        player spent points 

        item:
        what player will buy with money
        
        Side effects:
            money value may change,
            player will aquire item, therefore game sate will be effected 
        
            

        """
    def cards(self, userchoice, mchoice):
        attack1 = 2
        attack2 = 3
        attack3 = 4
        if userchoice == attack1:



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
    







if __name__ == "__main__":
    main()