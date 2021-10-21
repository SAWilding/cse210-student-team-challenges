import random
class Words():
    """
    Stores the words and generates a word to be printed.

    Stereotype:
    Data Manipulator

    Attributes: 
    words: stores a list of possible words.
    current_word: stores the word that will be used for that session of play.
    letter_list: stores a list of each individual letter of the current word.
    dashed_list: stores a list of dashes equal to the length of letter_list.
    incorrect_guesses: stores the numbers of incorrect guesses by the player.
    """

    def __init__(self):

        self.words = ["mars", "astronaut", "space", "comet", "explore", "supernova", "telescope", "pluto"]
        self.current_word = random.choice(self.words)
        self.letter_list = []
        self.dashed_list = []
        self.incorrect_guesses = 0
    def split_word(self):
        """
        Splits the word into a list of individual letters.
        """
        self.letter_list = list(self.current_word)
    
    def create_dashed_list(self):
        """
        Create the dashed list and stores it into the dashed_list variable.
        """
        for _ in range(len(self.current_word)):
            self.dashed_list.append("_")

    def update_dashed_list(self, user_guess):
        """
        Updates the dashed list if the player guesses a correct letter.
        """
        for i in range(len(self.letter_list)):
            if self.letter_list[i] == user_guess:
                self.dashed_list.pop(i)
                self.dashed_list.insert(i, user_guess)
        if user_guess not in self.letter_list:
            self.incorrect_guesses += 1            

