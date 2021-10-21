from random import randint
from termcolor import colored
#display 

class Board():

    def __init__(self):
        self._items = {}
        self._code = 0
    def prepare(self, player):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
        """
        name = player.get_name()
        self._code = str(randint(1000, 10000))
        guess = "----"
        hint = colored("****", 'red')
        self._items[name] = [guess, hint]

    def update_guess(self, player, guess):
        '''Takes the guess from the user and makes the self.guess equal to that.'''
        name = player.get_name()
        self._items[name][0] = guess


    def update_hint(self, player, hint):
        name = player.get_name()
        self._items[name][1] = hint
        
    def create_board(self, player):
        name = player.get_name()
        guess = self._items[name][0]
        hint = self._items[name][1]
        board = f"Player {name}: {guess}, {hint}"
        return board
        
    def _create_hint(self, code, guess):
        """Generates a hint based on the given code and guess.

        Args:
            self (Board): An instance of Board.
            code (string): The code to compare with.
            guess (string): The guess that was made.

        Returns:
            string: A hint in the form [xxxx]
        """ 
        hint = ""
        for index, letter in enumerate(guess):
            if code[index] == letter:
                hint += colored("x", 'green')
            elif letter in code:
                hint += colored("o", 'yellow')
            else:
                hint += colored("*", 'red')
        return hint