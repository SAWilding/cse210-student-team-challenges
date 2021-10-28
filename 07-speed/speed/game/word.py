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
        # for _ in range(5):
        self.get_random_word()
        self.set_text(self.word)
        self.set_position(Point(constants.MAX_X - 200, 50))
        self.set_velocity(Point(-1, 0))





#test=Words()
#test.prepare()