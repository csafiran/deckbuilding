import random

#####
# User Interface
#####

class BoardState:
    """
    Class that represents the board of the deckbuilding game.
    
    Attributes:
        points (int): Representing the amount of points avalible in the 
        point pool. When it reaches 0, the game is over. 
        monster_cards (list): Will contain a list of monster cards that
        can be defeated.
        center_cards (list): Will contain a list of purchasable cards
    """
    def __init__(self):
        """
            Creates and initilizes attributes.

            Args:
                self: An instance of the BoardState class.
                points (int): Representing the amount of points avalible in the 
                point pool. When it reaches 0, the game is over.
                monster_cards (list): Will contain a list of monster cards that
                can be defeated.
                center_cards (list): Will contain a list of purchasable cards
            
            Side effects: Creates an instance variable
                    
        """
        self.points = 60
        self.monster_cards = [None for i in range(6)]
        self.center_cards = [None for i in range(6)]
        for i in range(6):
            self.renew_card(i)
        for i in range(6):
            self.renew_monster(i)
    
    def renew_card(self,index):
        """
            Creates and replaces bought cards based on their index.

            Args:
                index (int): Representing the position of the bought card. 
                    
        """
        heroes = [Card("Larry,P,2,0,2"), Card("Izulu,P,3,2,0"), \
            Card("Fin,P,4,0,3"), Card("Azule,P,6,3,0"), Card("Biki,P,7,5,0"),\
                Card("Verdant,P,7,5,5"), Card("Cetra,P,8,6,0"),\
                    Card("Emri the Shadowslayer,P,8,0,6"),\
                        Card("Master Dhartha,P,8,7,0"), Card("P.R.I.M.E,P,10,9,9")]
        #switch from uniform probability
        card = random.choices(heroes,weights=[4,4,3,3,2,2,1,1,1,1])[0]
        #add new_card to the list
        self.center_cards[index] = card
         
    def renew_monster(self, index):
        """
            Creates and replaces defeated monsters based on their index.

            Args:
                index (int): Representing the position of the defeated monster. 
                    
        """
        monster_names = {1:"Fire Spirt", 2:"Ice Golem", 3:"Goblin Brusier", \
                         4:"Electro Wizard", 5:"Witch", 6:"Electro Giant", 7:"Dark Mega Knight", 8:"Golem", 9:"Leviathan", 10:"Ender of Worlds"}
        #switch from uniform probability
        cost = random.choices(range(1, 10),weights=[3,3,4,5,5,2,2,1,1])[0]
        #add new_card to the list
        self.monster_cards[index] = Card(f"{monster_names[cost]},M,{cost},0,0") 
   
    def __str__(self):
        """
            Displays both, the monster row and the purchasable cards row, to the
            user.

            Side effects: Prints both rows to the user.
            
            Returns: The points remaining in the point pool. 
                    
        """
        # Display both card rows
        #print(self.monster_cards)
        #print(self.center_cards)
        
        # Display current point pool level
        return f" Points remaining: '{self.points}'"

#####
# Game Logic
#####

def remove_choice(population, k):
    """
        Removes the respective (monster or pruchasable) card from their
        respective rows
        
        Args: 
            population (list): Represents the card
            k (int): The position of the selected card
        
        
        Returns: The removed card from the list        
    """
    # function for selecting removing selected card
    choice = []
    for i in range(k):
        choice.append(population.pop(random.randrange(len(population))))
    return choice


class Player:
    """Class for a deckbuilding player.
    
    Attributes:
        name (str): The player's name.
        points (int): The player's total points.
        path (filepath): The filepath to each player's respective deck. Stored 
        as a text file.
        
    """
    def __init__(self, name, path):
        """
            Creates and initilizes attributes.

            Args:
                self: An instance of the Player class.
                name (string): The player's name
                points (int): The player's total points.
                path (filepath): The filepath to each player's respective deck. Stored 
                as a text file.
            
            Side effects: Rewrites the starter deck file for each player.
                    
        """
        self.name = name
        self.points = 0
        self.path = path
        self.discard_pile = []
        with open(self.path, "w", encoding = "UTF-8") as f:
            f.write(
            '''
            Money Card, P, 0, 1, 0
            Money Card, P, 0, 1, 0
            Money Card, P, 0, 1, 0
            Money Card, P, 0, 1, 0
            Money Card, P, 0, 1, 0
            Money Card, P, 0, 1, 0
            Money Card, P, 0, 1, 0
            Money Card, P, 0, 1, 0
            Combat Card, P, 0, 0, 1
            Combat Card, P, 0, 0, 1
            ''')
    
    def turn(self, state):
        """Take a turn. Draing the player's hand and having the player make 
        decisions with their hand.
        
        Args:
            state (GameState): a snapshot of the current state of the game.
            
        Side Effects:
            May print gamestate or other UI information
        """
        print(f"{self.name}'s turn")
        
        hand = self.draw()
        
        # calculate total money availble
        money = sum([card.money_payout for card in hand])

        # calculate total kombat available
        combat = sum([card.combat_payout for card in hand])

        # display state
        print("Hand:")
        for card in hand:
            print(f"* {card}")

        # UI
        cont = True
        while cont:
            print(f"Board: {state}")
            print(f"Remaining Money: {money}")
            print(f"Remaining Combat: {combat}")
            decision = input(f"What are you going to do? Attack [A], Buy [B], or Change turn [C]? ")
            if decision == 'A':
                index = int(input("Which card are you going to attack? [1-6]")) - 1
                card = state.monster_cards[index]
                if card.cost > combat:
                    print("You lack the necessary combat points!")
                else:
                    self.points += card.cost + 1
                    state.renew_monster(index)
                    state.points -= card.cost + 1
                    combat -= card.cost
                
            elif decision == 'B':
                index = int(input("Which card would you like to buy? [1-6]")) - 1
                card = state.center_cards[index]
                if card.cost > money:
                    print("You lack the necessary funds!")
                else:
                    state.renew_card(index)
                    money -= card.cost
                    self.discard_pile.append(card)
                
            elif decision == 'C':
                cont = False
            
            else:
                print("Learn to read, moron")
                

        # discard hand at end of turn
        self.discard_pile.extend(hand)
        
    def draw(self):
        """
        Function to draw five cards from the player's deck to their hand. 
        Adds them to the player's discard pile when turn is over. This function 
        will automatically take cards from the player's discard pile when the deck
        has zero cards and still needs to draw one or more.
        
        Returns: Returns "cards" as a list.
        """

        # load deck from file
        deck = []
        
        with open(self.path, encoding="UTF-8") as f:
            for line in f:
                line = line.strip()  # remove leading and trailing whitespace
                if len(line) > 0:    # ignore blank lines
                    self.deck.append(Card(line))

        # draw 5 cards or remaining deck, which ever is smaller
        hand = remove_choice(self.deck, min(5, len(self.deck)))

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
                            
    def calc_score(self):
        """
        Calculates current score
        
        Returns:
            The final score of the game
        """    
        return 0
    # TODO Stubby. Zero is a test value.

class Card:
    """Class for indexing and parsing cards.
    
    Attributes:
        card_string (string): The card string that we will parse.
        
    """
    def __init__(self, card_string):
        """
            Creates and initilizes attributes.

            Args:
                self: An instance of the Card class.
                card_string (string): The card string that we will parse.
                                
        """
        #print(f"Card.__init__({card_string}") for debugging
        
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
        """
            Displays the player's name and their total money and combat for that
            turn.
            
            Returns: The player's name and their total money and combat for that
            turn. 
                    
        """
        return f'{self.name}: {max(self.money_payout, self.combat_payout)}'
    
    def __repr__(self):
        """
            
            Returns: The parsing iterator. 
                    
        """
        return self.card_string

def main():
    """
    The main function is where users enter their name, the GameState is 
    constructed, the loop of the player turns, and the winners are declared.

    Side effects:
    Asks for the users names and prints the winners of the game.
    """
    #Main menu: We need two player names
    p1name = input("Player 1, enter your name: ")
    p2name = input("Player 2, enter your name: ")
    
    #Construct the GameState
    board = BoardState()
    players = [Player(p1name, "player1Deck.txt"), Player(p2name, "player2Deck.txt")]
    turn = 0
    print(f"welcome to the game {p1name}, and {p2name}")
    #Gameloop - Alternate player1 and player2 turn until game is over
    while turn != 0 or board.points > 0:
        players[turn].turn(board)
        turn = (turn + 1) % len(players)
        
    #Declare winner (cleanup: reset temp files)
    max_score = -1
    winners = []
    for player in players:
       score = Player.calc_score()
       if score > max_score:
           winners = [player]
       elif score == max_score:
          winners.append(player)
    print("Winner(s): " + str(winners))
    # TODO: Clean up??

if __name__ == "__main__":
    main()
