# code to implement a number guessing game :)

# use random module to generate random number to guess
import random

# function that contains logic to check whether to begin the game or not
def beginGame():

    # boolean function to return to determine to begin game or not
    begin = False
    # get user response on asking if they want to play or not
    response = input("Would you like to play?(Y/N) ")
    
    # turn reponse to lower case to remove case-sensitivity    
    # if player says yes, return true and begin game
    if response.lower() == 'y':

        begin = True
        return begin
    else:
        
        return begin

# contains logic on how the game will work
def gameLogic(start):

    if start:

        # initialise the number to guess and boolean to keep track if player wins
        numberToGuess = random.randint(0,10)
        correct = False

        # variable to store number of attempts
        attempts = 0

        # keep asking for user input until player wins
        while correct == False:

            playerGuess = input("Enter a number from 1 to 10: ")
            # turn input to integer
            guessAsInt = int(playerGuess)
            # increment attempts
            attempts = attempts + 1


            # player gets the number, correct becomes true
            if guessAsInt == numberToGuess:
                
                print("Congrats you win!")
                print("It took " + str(attempts) + " attempt/s")
                correct = True

            elif guessAsInt > numberToGuess and guessAsInt <= 10:

                # player guess is higher than actual number
                print("lower")

            elif guessAsInt < numberToGuess and guessAsInt >= 0:

                # player guess is lower than actual number
                print("higher")

            else:

                # invalid input
                print("enter valid number please")        



# call functions to play game
start = beginGame()

gameLogic(start)
