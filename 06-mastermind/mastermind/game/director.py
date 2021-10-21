from game.board import Board
from game.console import Console
from game.guess import Guess
from game.player import Player
from game.roster import Roster
from termcolor import colored


class Director():
    def __init__(self):
        
        self._roster = Roster()
        self._console = Console()
        self._guess = Guess()
        self._board = Board()        

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
        
        self._console.write("-"*20)   
        for player in self._roster.players:
            self._board.prepare(player)
            board = self._board.create_board(player)
            self._console.write(board)
        self._console.write("-"*20)
        self._console.write(self._board._code)

    def _get_inputs(self):
        

        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        guess = self._console.read(colored("What's your guess? ", 'green', attrs=['bold']))
        self._guess.set_guess(guess) 
        self._board.update_guess(player, guess)


    def _do_updates(self):
        
        player = self._roster.get_current()

        self._roster.next_player()
        code = self._board._code
        guess = self._guess.get_guess()
        hint = self._board._create_hint(code, guess)
        self._board.update_hint(player, hint)
        self._keep_playing = self._guess.check_guess(code)

    def _do_outputs(self):
        
        self._console.write("-"*20)
        for player in self._roster.players:
            board = self._board.create_board(player)
            self._console.write(board)
        self._console.write("-"*20)
