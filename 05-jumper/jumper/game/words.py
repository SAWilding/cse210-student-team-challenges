import random
class Words():
    """
    Stores the words and generates a word to be printed.
    """

    def __init__(self):

        self.words = ["mars", "astronaut", "space", "comet", "explore", "supernova", "telescope", "pluto"]
        self.current_word = random.choice(self.words)

    def split_word(self):
        """
        Splits the word into a list of individual letters.
        """
        letter_list = list(self.current_word)
        return letter_list

    def word_length(self):
        """
        Determines the length of the word.
        """
        return len(self.current_word)
    
