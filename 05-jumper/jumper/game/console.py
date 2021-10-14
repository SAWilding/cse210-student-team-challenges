from game.jumper import Jumper

class Console():
    """
    Prints stuff to the screen.
    """
    def __init__(self):
        self.letter_list = ["t","e","s","t","b","l"]
        self.guess_list = [0,0,0,1,1,0]

        user_incorrect_number_of_guesses = 0
        self.user_guess = ""
        self.jumper = Jumper()
        

    def get_user_input(self):
        """
        Get guess letter guess from the user.
        """
        self.jumper.user_guess = input("Guess a letter [a-z]: ")

        return self.jumper.user_guess

    


    def display_board(self):
        """
        Inilize Variables
        """
        user_incorrect_number_of_guesses = 3


        """
        Displays the jumper character.
        """
        #starting Header for image
        print('_ _ _ _ _ ')
        print('\n')

        #Sets the array to be used inthis fuction to be that Of the selected image
        #that Is received from the Jumper Class
        Array_of_Character = self.jumper.character

        #Gets the Length of the Array so that the "for loop" can iterate over the correct length of the image
        length = len(Array_of_Character)

        #reveres the the array so that there can be easy removal of each of the top section sof the image 
        Array_of_Character = Array_of_Character[::-1]

        #prints the array fromtop to bottom, if the user has any number of incorrect guesses, this will automatically 
        #remove the most top section of the image of the character.
        for x in reversed(range(length - user_incorrect_number_of_guesses)):
            print(Array_of_Character[x])

        
        print('\n')
        print('^^^^^')

        pass



    def display_word(self):
        """
        Displays the dash list.
        """

        for x in range(len(self.letter_list)):

             if (self.guess_list[x] == 1):
                print(self.letter_list[x], end=" ")
             else:
                    print("_ ", end="")
        print("")
            

        pass
