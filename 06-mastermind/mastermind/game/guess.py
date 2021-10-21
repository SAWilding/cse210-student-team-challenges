#called once at start

class Guess():
    def __init__(self):
        self.current_guess = 0
        self.p1_guess = 0
        self.p2_guess = 0

    #sets the guess 
    def set_guess(self, user_guess):
        self.current_guess = user_guess
    
    def get_guess(self):
        return self.current_guess
