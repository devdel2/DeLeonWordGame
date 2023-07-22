"""
    Name: Devin DeLeon
    Date: 7/20/2023
    Description: This file will handle the main game logic and allow for guessing and winning/lose
    the game.
"""


# will check to see if the guess is apart of the alphabet
def is_user_guess_alpha(user_guess):
    if user_guess.isalpha():
        return True
    else:
        return False


# will gather the users guess
def get_user_guess():
    user_guess = input("Please enter a letter for your guess: ")
    while not is_user_guess_alpha(user_guess):
        print(f"\n{user_guess} is not a letter of the alphabet.\nThis will not count as a strike.\nPlease try again.\n")
        user_guess = input("Please enter a letter for your guess: ")
    return user_guess.upper()


# this will check if the user guess is in the chosen word
def is_user_guess_in_word(user_guess, rand_word):
    if user_guess in rand_word:
        print(f'you guessed {user_guess} and it IS in {rand_word}')
        return True
    else:
        print(f'{user_guess} is not in the word.')
        return False
