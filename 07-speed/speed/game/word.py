import os
import random

from raylibpy import get_shader_default
from game.actor import Actor
from game.point import Point
from game.score_board import ScoreBoard
from game import constants

class Word(Actor):
    def __init__(self):
        super().__init__()
        self._add_longest_word = False
        self.word = ""
        self.words_list= []
        self.PATH = os.path.dirname(os.path.abspath(__file__))
        self.lines = open(self.PATH + "/words.txt").read().splitlines()
        self._prepare()

    def get_random_word(self):
        myline =random.choice(self.lines)
        self.word = myline
        self.words_list.append(self.word)

    def get_longest_word(self):
        self._add_longest_word = True
        print('word longest fucntion called')
        # self.word = "floccinaucinihilipilification"
        # self.words_list.append(self.word)

    def _prepare(self):
        if self._add_longest_word == True:
            print('true called')
            self.word = "floccinaucinihilipilification"
            self.words_list.append(self.word)
            self.set_text(self.word)
            self.set_position(Point(constants.MAX_X, random.randint(20, constants.MAX_Y - 50)))
            self.set_velocity(Point(random.randint(-2, -1), 0))
        elif self._add_longest_word == False:
            print('false called')
            self.get_random_word()
            self.set_text(self.word)
            self.set_position(Point(constants.MAX_X, random.randint(20, constants.MAX_Y - 50)))
            self.set_velocity(Point(random.randint(-2, -1), 0))

    def check_position(self):
        pass

    # def get_longest_word(self):
    #     return self.longest_word

    # def add_longest_word(self):
    #     self.words_list.append("floccinaucinihilipilification")


