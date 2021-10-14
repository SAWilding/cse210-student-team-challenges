import random
class Words():
    """
    Stores the words and generates a word to be printed.
    """

    def __init__(self):

        # self.words = ["mars", "astronaut", "space", "comet", "explore", "supernova", "telescope", "pluto"]
        self.words = ["mars"]
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
        for _ in range(len(self.current_word)):
            self.dashed_list.append("_")

    def update_dashed_list(self, user_guess):
        for i in self.letter_list:
            if self.letter_list[i] == user_guess:
                self.dashed_list.pop(i)
                self.dashed_list.insert(i, user_guess)
            else:
                self.incorrect_guesses += 1            

