import math

#####
# User Interface
#####

class Boardstate:
# this is where the UI would go. We plan on doing this part last.

#####
# Game Logic
#####

class GameState:
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
        

class Players:
    """Class for a deckbuilding player.
    
    Attributes:
        name (str): the player's name.
    """
    def __init__(self, name):
        self.name = name
    #We may need to initilize our deck, handle, and discard piles here as well
    
    def turn(self, state):
        """Take a turn.
        
        Args:
            state (GameState): a snapshot of the current state of the game.
        """
    def buy():
    #function that will represent what happens when a player purchases a card
    #from the center row
    
    def defeat():
    #function that will represent what happens when a player defeats a monster 
    #card from the center row
    
    def action():
    #function that will represent the actions the player does with their cards
    #in their hand