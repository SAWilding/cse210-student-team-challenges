import os
import random

class Words:
    def __inti__(self):
        self.words = []
        self.PATH = os.path.dirname(os.path.abspath(__file__))
        self.LIBRARY = open(self.PATH + "/words.txt")

    def get_Random_Word(self):
        print(self.LIBRARY)
        pass

test=Words()
test.get_Random_Word()