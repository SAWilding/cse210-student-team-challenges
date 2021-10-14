from game.dealer import Dealer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        dealer (Dealer): An instance of the class of objects known as Dealer.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 300
        self.dealer = Dealer()

    def can_play_again(self):
            """
            Checks to see if the player can play again.
            """
            if self.score <= 0:
                return False
            else:
                return True

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            # self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means dealing the card.
        Args:
            self (Director): An instance of Director.
        """
        self.dealer.get_card()
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.
        Args:
            self (Director): An instance of Director.
        """
        points = self.dealer.get_points()
        self.score += points
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the card that were rolled and the score.
        Args:
            self (Director): An instance of Director.
        """
        
        print(f"The card is:{self.dealer.card_active}")

        self.dealer.choice = input(f"Higher or lower? [h/l] ") # user_choice needs to be made in dealer.py
        
        print(f"\nNext card was: {self.dealer.card_next}")
        print(f"")
        
        self.do_updates() # moved do_updates so it will update points 

        print(f"Your score is: {self.score}")
        if self.can_play_again():
            choice = input("Keep Playing? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False