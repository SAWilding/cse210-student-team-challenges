import sys
from termcolor import colored, cprint
from random import randint
class Dealer():
    def __init__(self):
        self.card_active = 0
        self.points = 0
        self.choice = ""
        self.card_next = randint(1, 13)

    def get_user_choice(self):
        self.choice = input("Higher or lower? [h or l] ")  


    def get_points(self):
        """
        Keeps track of the number of points.
        """
        self.points = 0

        print_red = lambda x: cprint(x, 'red')
        print_green = lambda x: cprint(x, 'green')
        print_blue = lambda x: cprint(x, 'blue')

        if self.card_active < self.card_next and self.choice.lower() == "l": # sign was >
            self.points -= 75
            print_red("You were incorrect!")
        elif self.card_active > self.card_next and self.choice.lower() == "h": # sign was <
            self.points -= 75
            print_red("You were incorrect!")
        elif self.card_active > self.card_next and self.choice.lower() == "l": # sign was <
            self.points += 100
            print_green("You were correct!")
        elif self.card_active < self.card_next and self.choice.lower() == "h": # sign was >
            self.points += 100
            print_green("You were correct!")
        else:
            self.points += 0
            print_blue("The cards were the same.")
        return self.points

    def get_card(self):
        """
        Generates a random number between 1 and 13 for the card number.
        """
        self.card_active = self.card_next
        self.card_next = randint(1,13)
