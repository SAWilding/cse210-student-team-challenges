from game.console import Console
from game.jumper import Jumper
from game.words import Words

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        jumper (Jumper): An instance of the class of objects known as Jumper.
        words (Words): An instance of the class of objects known as Words.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.jumper = Jumper()
        self.words = Words()
        



    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self.words.create_dashed_list()
        self.words.split_word()
        self.console.display_list(self.words.dashed_list)

        self.console.display_board(self.jumper.character, self.words.incorrect_guesses)
        while self.jumper.keep_playing(self.words.dashed_list, self.words.incorrect_guesses):
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        self.console.display_board(self.jumper.character, self.words.incorrect_guesses)


    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. 
        Args:
            self (Director): An instance of Director.
        """
        self.console.get_user_input()
        
    def do_updates(self):
        """Updates the important game information for each round of play. 
        Args:
            self (Director): An instance of Director.
        """
        self.words.update_dashed_list(self.console.user_guess)
        

    def do_outputs(self):
        """Outputs the important game information for each round of play. 

        Args:
            self (Director): An instance of Director.
        """
        self.console.display_list(self.words.dashed_list)
        self.console.display_board(self.jumper.character, self.words.incorrect_guesses)
        print("Guessed letters:")
        self.console.display_list(self.console.user_guess_list)
