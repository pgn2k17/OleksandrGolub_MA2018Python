# Testing template for "Guess the number"

###################################################
# Student should add code for "Guess the number" here


# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import random
import math

# initializing global variables used in my code
num_range = 100
secret_number = 0
user_guess = 0
num_guesses = 7

# helper function to start and restart the game
def new_game():
    global secret_number, num_range, num_guesses
    secret_number = random.randrange(0, num_range)
    
    if num_range == 100:
        num_guesses = int(math.ceil(math.log(100, 2)))
    elif num_range == 1000:
        num_guesses = int(math.ceil(math.log(1000, 2)))
    
    print("\nA new game has started with a range from 0 to " + str(num_range))
    print("You have " + str(num_guesses) + " guesses remaining.")

# helper function to decrement guesses remaining
def decrement_guesses():
    global num_guesses
    num_guesses -= 1
    
    if num_guesses > 0:
        print("Remaining guesses: " + str(num_guesses))
    else:
        print("You lose!")
        new_game()

# define event handlers for control panel
def range100():
    global num_range
    num_range = 100
    new_game()
    
def range1000():
    global num_range
    num_range = 1000
    new_game()

def input_guess(guess):
    global secret_number, user_guess
    user_guess = int(guess)
    if user_guess < secret_number:
        print("\nHigher!")
        decrement_guesses()
    elif user_guess > secret_number:
        print("\nLower!")
        decrement_guesses()
    else:
        print("\nCorrect!")
        new_game()

# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
frame.add_button("Rangeis[0,100)", range100, 200)
frame.add_button("Rangeis[0,1000)", range1000, 200)
frame.add_input("Enter your guess", input_guess, 50)

# call new game and start frame
new_game()
frame.start()
