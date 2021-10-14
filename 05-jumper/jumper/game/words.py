import random
class Words():
    """
    Stores the words and generates a word to be printed.
    """

    def __init__(self):

        self.words = ["Mars", "astronaut", "space", "comet", "explore", "supernova", "telescope", "Pluto"]

    def split_word(self):
        """
        Splits the word into a list of individual letters.
        """
        current_word = random.choice(self.words)
        list(current_word)
        print(current_word)

    def word_length(self):
        """
        Determines the length of the word.
        """

    
