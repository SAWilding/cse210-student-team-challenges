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
            
        for player in self._roster.players:
            self._board.prepare(player)
            board = self._board.create_board()
            self._console.write(board)

        

    def _get_inputs(self):
        

        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        guess = self._console.read("What's your guess? ")
        self._guess.set_guess(guess) 

    def _do_updates(self):


        self._roster.next_player()
        code = self._board.code
        guess = self._board.guess
        guess = self._guess.get_guess()
        self._board.hint = self._board._create_hint(code, guess)

    def _do_outputs(self):
        

        board = self._board.create_board()
        self._console.write(board)

