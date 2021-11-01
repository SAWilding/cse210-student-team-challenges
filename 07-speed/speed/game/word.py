import os
import random
from game.actor import Actor
from game.point import Point
from game import constants

class Word(Actor):
    def __init__(self):
        super().__init__()
        self.word = ""
        self.words_list= []
        self.PATH = os.path.dirname(os.path.abspath(__file__))
        self.lines = open(self.PATH + "/words.txt").read().splitlines()
        self._prepare()



    def get_random_word(self):
        myline =random.choice(self.lines)
        self.word = myline
        self.words_list.append(self.word)


    def _prepare(self):
        self.get_random_word()
        self.set_text(self.word)
        self.set_position(Point(constants.MAX_X, random.randint(20, constants.MAX_Y - 50)))
        #creates the random integer for the x and y velocity
        x = random.randint(-3, 3)
        y = random.randint(-3, 3)
        #this will ensure that there is never a velocity of zero
        if x == 0:
            x = x + 1
        if y == 0:
            x = y + 1    
        #Set the velocity that is created
        self.set_velocity(Point(x, y))

    def check_position(self):
        pass





#test=Words()
#test.prepare()