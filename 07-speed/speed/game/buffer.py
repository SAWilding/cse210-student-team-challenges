import random
import raylibpy
from game import constants
from game.actor import Actor
from game.point import Point
class Buffer(Actor):
    def __init__(self):
        super().__init__()
        self._prepare()
        self._content = ""


    def _prepare(self):
        self._content = ""
        self.set_text(f"Buffer: {self._content}")
        self.set_position(Point(0, constants.MAX_Y - 25))

    def _update_buffer(self):
        key = raylibpy.get_key_pressed()
        
        if key > 0:
            letter = chr(key)
            self._content += letter
            self.set_text(f"Buffer: {self._content}")
        if key == 13:
            self._clear_buffer()

    def _clear_buffer(self):
        self._content = ""
        self.set_text(f"Buffer: {self._content}")