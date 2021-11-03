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

        """
            This will get the current input rom the player, assumin g
        """
        #test input
        place_player_input_string_here = "lolJerryovetomlol"

        """
            This will take the player stings and make them lower incase the player
            Presses the shift key or caps the wrong letter of the word.
        """
        place_player_input_string_here = place_player_input_string_here.lower()

        #debug print string
        print(place_player_input_string_here)

        for x in range(len(temp_word_list_check)):

            if  temp_word_list_check[x] in place_player_input_string_here:
                #this will remove the correct word from the players typed out string if it is correct
                place_player_input_string_here = place_player_input_string_here.replace(temp_word_list_check[x], '')
                #debug print string
                print(place_player_input_string_here)


    pass