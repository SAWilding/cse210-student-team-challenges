from game.board import Board
from game.console import Console
from game.guess import Guess
from game.player import Player
from game.roster import Roster


class Director():
    def __init__(self):
        
        self._roster = Roster()
        self._console = Console()
        self._guess = Guess()
        self._board = Board()
        self._items = []
        

        self._keep_playing = True

    def start_game(self):
        
        self._prepare_game()
        
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()


    def _prepare_game(self):
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)



    def _get_inputs(self):
        self._board.prepare(self._roster.get_current())
        pass

    def _do_updates(self):
        print(Player.get_name(self._roster.get_current()))

        #this will filp flop between player one and player two
        self._roster.next_player()


        pass

    def _do_outputs(self):
        pass

