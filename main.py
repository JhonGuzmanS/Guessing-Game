#A simple game that will generate a random number between 1 and 100, inclusively, and the user will have 5 guesses to find the correct number
# generate a random number, count the amount of guesses, let user give input until number of guesses run out

import random
# Helper functions
def generate_num():
    return random.randint(1, 99)

def check_input(input, answer):
    if input > answer:
        print("Too high!")
    elif input < answer:
        print("Too low!")
    return input == answer

# Start of main
def main():
    guesses = 5
    answer = generate_num()
    found = False
    while not found and guesses > 0:
        inp = int(input("Guess a number between 0 and 100: "))
        found = check_input(inp, answer)
        guesses -= 1
    if found:
        print(f"Congrats! The correct number is {answer}!")
    else:
        print(f"Out of guesses. The correct number was {answer}")
        
# Start of program
main()