from game.words import Words

class Jumper():
    """
    Creates the jumper character
    """

    def __init__(self):
        self.character = [" ___ ", "/___\ ", "\   /", " \ / ", "  0  ", " /|\ ", " / \ "]
        self.user_guess = ""


    # def check_letter_in_list(self, letter_list, user_guess):
    #     temp_list = []
    #     for i in letter_list:
    #         if user_guess == letter_list[i]:



