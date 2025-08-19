#A simple game that will generate a random number between 1 and 100, inclusively, and the user will have 5 guesses to find the correct number
# generate a random number, count the amount of guesses, let user give input until number of guesses run out
# Adjust the range, adjust the amount of guesses.

import random
# Helper functions
def generate_num(min=0, max=100):
    return random.randint(min, max)

def check_input(input, answer):
    if input > answer:
        print("Too high!")
    elif input < answer:
        print("Too low!")
    return input == answer

# Returns adjusted values
def settings():
    guesses = int(input("Input the number of guesses(Default is 5): "))
    min = int(input("Input the minimum number(Default is 0): "))
    max = int(input("Input the maximum number(Default is 100): "))
    return guesses, min, max

# Gameplay
def game(guesses, min, max):
    answer = generate_num(min, max)
    found = False
    while not found and guesses > 0:
        inp = int(input(f"Guess a number between {min} and {max}: "))
        found = check_input(inp, answer)
        guesses -= 1
    if found:
        print(f"Congrats! The correct number is {answer}!")
    else:
        print(f"Out of guesses. The correct number was {answer}")

# Start of main
def main():
    guesses = 5
    min = 0
    max = 100
    end_game = False
    while not end_game:
        start_game = input("Would you like to go to the settings? (Y/N): ")
        if start_game.lower() == 'y':
            guesses, min, max = settings()
        game(guesses, min, max)
        end = input("Would you like to play again? (Y/N): ")
        if end.lower() == 'n':
            end_game = True
        
# Start of program
main()