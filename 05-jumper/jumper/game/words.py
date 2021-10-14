import random
class Words():
    """
    Stores the words and generates a word to be printed.
    """

    def __init__(self):

        self.words = ["Mars", "astronaut", "space", "comet", "explore", "supernova", "telescope", "Pluto"]
<<<<<<< HEAD
        self.current_word = random.choice(self.words)


=======
        
>>>>>>> 1068fd3b8de1dd3bc7cb90473b2229a141e0f112
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

    
