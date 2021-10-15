from game.words import Words

class Jumper():
    """
    Creates the jumper character

    Stereotype:
    Player

    Attributes:
    character: stores a list that displays the jumper character.
    """

    def __init__(self):
        self.character = [" ___ ", "/___\ ", "\   /", " \ / ", "  0  ", " /|\ ", " / \ "]

    def keep_playing(self, dashed_list, incorrect_guesses):
        """
        Determines if the player can keep playing or not.
        """
        if "_" not in dashed_list:
            print()
            print("You won!!")
            print()
            return False
        elif incorrect_guesses == 4:
            self.character[4] = "  x  "
            print()
            print("You lost!!")
            print()
            return False
        else:
            return True
        







