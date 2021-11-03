#This is an import check system for Jonathans Computer
#If the import for the file path fails, it will go to a normal raylibpy import
# '''
try:
    import os
    os.environ["RAYLIB_BIN_PATH"] = r"C:\Users\jlgun\AppData\Local\Programs\Python\Python39\Lib\site-packages\raylib-2.0.0-Win64-mingw\lib"  #gitignore
    import raylibpy 
except Exception as e:
    print(e)
    try:
        import os
        os.environ["RAYLIB_BIN_PATH"] = r"C:\Users\Sam\AppData\Local\Programs\Python\Python39\Lib\site-packages\raylib-2.0.0-Win64-mingw\lib"
        import raylibpy
    except Exception as e:
        print(e)
    else:
        import raylibpy
        print("Default import raylibpy Called")
else:
    import raylibpy
    print("Default import raylibpy Called")
import os
os.environ["RAYLIB_BIN_PATH"] = r"C:\Users\jlgun\AppData\Local\Programs\Python\Python39\Lib\site-packages\raylib-2.0.0-Win64-mingw\lib"  #gitignore
# '''

import raylibpy
from time import sleep

from game import constants

from game.score_board import ScoreBoard

from game.buffer import Buffer

from game.word import Word

from random import randint

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        food (Food): The snake's target.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        snake (Snake): The player or snake.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score_board = ScoreBoard()
        self._buffer = Buffer()
        self._words = [Word(), Word(), Word(), Word(), Word()]
        self._words_to_remove = []
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        print("Starting game...")
        self._output_service.open_window("Speed")
        self._input_service.check_word_list()
        
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

            if self._input_service.window_should_close():
                self._keep_playing = False

        print("Game over!")

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """


    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self.handle_word_generation() 
        for word in self._words:
            self.handle_word_deletion(word)
            self._output_service.draw_actor(word)
            word.move_next() 
            self.check_buffer_for_word(word)
        self._buffer._update_buffer()

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._buffer)
        self._output_service.draw_actor(self._score_board)
        self._output_service.flush_buffer()



    def handle_word_generation(self):
        chance = randint(1, 100)
        if chance <= 1:
            self._words.append(Word())

    def handle_word_deletion(self, word):
        position = word.get_position()
        position_x = position.get_x()
        if position_x == 0:
            self._words.remove(word)
            self._score_board.subtract_points(len(word.word))
            
    def check_buffer_for_word(self, word):
        key = raylibpy.get_key_pressed()
        if raylibpy.is_key_pressed(257):
            if word.word in self._buffer._content:
                self._words.remove(word)
                self._score_board.add_points(len(word.word))
