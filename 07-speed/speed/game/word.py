import os
import random
from game.actor import Actor

class Words(Actor):
    def __init__(self):
        super().__init__()
        self.word = ""
        self.words_list= []
        self.PATH = os.path.dirname(os.path.abspath(__file__))
        self.lines = open(self.PATH + "/words.txt").read().splitlines()



    def get_random_word(self):
        myline =random.choice(self.lines)
        self.word = myline
        self.words_list.append(self.word)


    def prepare(self):
        for _ in range(5):
            self.get_random_word()





#test=Words()
#test.prepare()