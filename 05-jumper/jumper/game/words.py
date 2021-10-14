import random
class Words():
    """
    Stores the words and generates a word to be printed.
    """

    def __init__(self):

        self.words = ["Mars", "astronaut", "space", "comet", "explore", "supernova", "telescope", "Pluto"]
        self.current_word = random.choice(self.words)


    def split_word(self):
        """
        Splits the word into a list of individual letters.
        """
        letter_list = list(self.current_word)
        print(letter_list)

    def word_length(self):
        """
        Determines the length of the word.
        """

    
