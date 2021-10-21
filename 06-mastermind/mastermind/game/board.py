from random import randint
#display 

class Board():

    def __init__(self):
        pass
        self.name = ""
        self.code = 0
        self.guess = ""
        self.hint = ""

    def prepare(self, player):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
        """
        self.name = player.get_name()
        self.code = str(randint(1000, 10000))
        self.guess = "----"
        self.hint = "****"
        
    def create_board(self):
        board = f"Player {self.name}: {self.guess}, {self.hint}"
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
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return hint