from game.words import Words

class Jumper():
    """
    Creates the jumper character
    """

    def __init__(self):
        self.character = [" ___ ", "/___\ ", "\   /", " \ / ", "  0  ", " /|\ ", " / \ "]
        self.user_guess = ""
        self.incorrect_amount = 0


    def check_letter_in_list(self):
        pass


