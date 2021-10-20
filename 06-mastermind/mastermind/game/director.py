class Director():
    def __init__(self):
        
        self._keep_playing = True

    def start_game(self):
        
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()


    def _prepare_game(self):
        pass

    def _get_inputs(self):
        pass

    def _do_updates(self):
        pass

    def _do_outputs(self):
        pass

