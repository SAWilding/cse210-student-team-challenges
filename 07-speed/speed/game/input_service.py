import sys
from game.point import Point
import raylibpy

class InputService:
    """Detects player input. The responsibility of the class of objects is
    to detect player keypresses and translate them into a point representing
    a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
        _current (Point): The last direction that was pressed.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self._current = Point(1, 0)
        




    def window_should_close(self):
        """
        Determines if the user is trying to close the window
        """
        return raylibpy.window_should_close()


    def check_word_list(self):
        #get current word list.
        temp_word_list_check = ["tom", "jerry", "move"]
        compare_list = "".join(temp_word_list_check)
        """
            This will get the current input rom the player, assumin g
        """
        place_player_input_string_here = "jerry"


        if place_player_input_string_here in compare_list:
            print('Success phase 1')
            for i in place_player_input_string_here:
                if i == compare_list:
                    print('Success!')
        else:
            print("failed!!!")

        pass