class Console():
    """
    Prints stuff to the screen.
    """
    def __init__(self):
        self.user_guess_list = []
        self.user_guess = ""

    def get_user_input(self):
        """
        Get guess letter guess from the user.
        """
        self.user_guess = input("Guess a letter [a-z]: ")
        self.user_guess_list.append(self.user_guess)

    def display_board(self, character, incorrect_guesses):
        """
        Inilize Variables
        """


        """
        Displays the jumper character.
        """

        #Sets the array to be used inthis fuction to be that Of the selected image
        #that Is received from the Jumper Class
        Array_of_Character = character

        #Gets the Length of the Array so that the "for loop" can iterate over the correct length of the image
        length = len(Array_of_Character)

        #reveres the the array so that there can be easy removal of each of the top section sof the image 
        Array_of_Character = Array_of_Character[::-1]

        #prints the array fromtop to bottom, if the user has any number of incorrect guesses, this will automatically 
        #remove the most top section of the image of the character.
        for x in reversed(range(length - incorrect_guesses)):
            print(Array_of_Character[x])

        
        print('\n')
        print('^^^^^')

    def display_list(self, list):
        for i in list:
            print(i, end=" ")
        print("\n")



    # def display_word(self, letter_list, guess_list):
    #     """
    #     Displays the dash list.
    #     """

    #     for x in range(len(letter_list)):

    #          if (guess_list[x] == 1):
    #             print(letter_list[x], end=" ")
    #          else:
    #             print("_ ", end="")
    #     print()
            

