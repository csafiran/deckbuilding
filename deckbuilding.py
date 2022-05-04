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
#        money = addMoney(hand)
#        kombat = addKombat(hand)
 #       chooseActions(self, state, money, kombat)
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

        randomTextList = random.sample(textList,len(textList))
        playerHandDraw = []

        while len(randomTextList) > 5:
            for line in randomTextList:
                for i in line:
                    playerHandDraw.append(i)
                    textList.pop()
                    randomTextList.pop()

        while len(randomTextList)<=4:
            for line in randomTextList:
                for i in line:
                    playerHandDraw.append(i)
                    textList.pop()
                    randomTextList.pop()
                    
        print(playerHandDraw)
                            

        
    
        
    
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
    
#    def battlecard(self):


#        if userchoice == attack1:
#            pass




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
        
#def test1():
   # print("starttest1")
   # player117 = Player("John", "playerDeck.txt")
    #print(player117.draw())    
    #print("endtest1")   
        
def main():
    """
    The main function is mainly used to call other functions and run our game.

    return:
    it will return the state of the game

    Side Facts:
    it will print the info of the game.
    """
    #m1 = Monster(random.randint(1,6), random.randint(1,5))
    #m2 = Monster(random.randint(1,6), random.randint(1,5))
    #m3 = Monster(random.randint(1,6), random.randint(1,5))
    #m4 = Monster(random.randint(1,6), random.randint(1,5))
    #m5 = Monster(random.randint(1,6), random.randint(1,5))
    #monster5 = []
    #player1 = Player("tmz")
    #player2 = Player("sss")
    #while True:
    #    us = GameAction.menu
    point = 0
    money = 0
    monster = 3

    print("wecome to the deckbuilding game!")
    while True:
        attack1 = random.randint(1,5)
        attack2 = random.randint(1,5)
        attack3 = random.randint(1,5)
        attack4 = random.randint(1,5)
        attack5 = random.randint(1,5)
        print("you only have 5 attack cards and you need to kill a monster to get honor")
        print(f"1.attack = [{attack1}]")
        print(f"2.attack = [{attack2}]")
        print(f"3.attack = [{attack3}]")
        print(f"4.attack = [{attack4}]")
        print(f"5.attack = [{attack5}]")
        us = input("please tell me which card would you like to play!")
        if int(us) == 1:
            if attack1 < monster:
                print(f"you still need {monster - attack1} point to kill the monster, which another card would you like to use ")
                print(f"1.attack = [{attack1}]")
                print(f"2.attack = [{attack2}]")
                print(f"3.attack = [{attack3}]")
                print(f"4.attack = [{attack4}]")
                print(f"5.attack = [{attack5}]")
                lol = input()
                if int(lol) > 0:
                    print("you have killed the monster!")
                    point += 5
                    print(f"now you have {point} honor!")
                    if point >= 30:
                        print("you win!!!")
                        break
                    
            else:



                point += 5
                print(f"now you have {point} honor!")
                if point >= 30:
                    print("you win!!!")
                    break
                print("which card would you like to use next?")
        if int(us) == 2:
            if attack2 < monster:
                print(f"you still need {monster - attack2} point to kill the monster, which another card would you like to use ")
                print(f"1.attack = [{attack1}]")
                print(f"2.attack = [{attack2}]")
                print(f"3.attack = [{attack3}]")
                print(f"4.attack = [{attack4}]")
                print(f"5.attack = [{attack5}]")
                lol = input()
                if int(lol) > 0:
                    print("you have killed the monster!")
                    point += 5
                    print(f"now you have {point} honor!")
                    if point >= 30:
                        print("you win!!!")
                        break
            else:



                point += 5
                print(f"now you have {point} honor!")
                if point >= 30:
                    print("you win!!!")
                    break
                print("which card would you like to use next?")
        if int(us) == 3:
            if attack3 < monster:
                print(f"you still need {monster - attack3} point to kill the monster, which another card would you like to use ")
                print(f"1.attack = [{attack1}]")
                print(f"2.attack = [{attack2}]")
                print(f"3.attack = [{attack3}]")
                print(f"4.attack = [{attack4}]")
                print(f"5.attack = [{attack5}]")
                lol = input()
                if int(lol) > 0:
                    print("you have killed the monster!")
                    point += 5
                    print(f"now you have {point} honor!")
                    if point >= 30:
                        print("you win!!!")
                        break
            else:



                point += 5
                print(f"now you have {point} honor!")
                if point >= 30:
                    print("you win!!!")
                    break
                print("which card would you like to use next?")
        if int(us) == 4:
            if attack4 < monster:
                print(f"you still need {monster - attack4} point to kill the monster, which another card would you like to use ")
                print(f"1.attack = [{attack1}]")
                print(f"2.attack = [{attack2}]")
                print(f"3.attack = [{attack3}]")
                print(f"4.attack = [{attack4}]")
                print(f"5.attack = [{attack5}]")
                lol = input()
                if int(lol) > 0:
                    print("you have killed the monster!")
                    point += 5
                    print(f"now you have {point} honor!")
                    if point >= 30:
                        print("you win!!!")
                        break
            else:



                point += 5
                print(f"now you have {point} honor!")
                if point >= 30:
                    print("you win!!!")
                    break
                print("which card would you like to use next?")
        if int(us) == 5:
            if attack5 < monster:
                print(f"you still need {monster - attack5} point to kill the monster, which another card would you like to use ")
                print(f"1.attack = [{attack1}]")
                print(f"2.attack = [{attack2}]")
                print(f"3.attack = [{attack3}]")
                print(f"4.attack = [{attack4}]")
                print(f"5.attack = [{attack5}]")
                lol = input()
                if int(lol) > 0:
                    print("you have killed the monster!")
                    point += 5
                    print(f"now you have {point} honor!")
                    if point >= 30:
                        print("you win!!!")
                        break
            else:



                point += 5
                print(f"now you have {point} honor!")
                if point >= 30:
                    print("you win!!!")
                    break
                print("which card would you like to use next?")
            
        






    








if __name__ == "__main__":
    #test1()
    main()