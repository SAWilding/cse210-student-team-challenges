import os

MAX_X = 600
MAX_Y = 400
FRAME_RATE = 60
FRAME_LENGTH = 0.08
STARTING_WORDS = 5
DEFAULT_TEXT_OFFSET = 5
DEFAULT_FONT_SIZE = 20
PATH = os.path.dirname(os.path.abspath(__file__))
LIBRARY = open(PATH + "/words.txt").read().splitlines()
