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
        return True
    else:
        return False


def reveal_letter_in_word(user_guess, rand_word, blank_spaces):
    for i in range(len(rand_word)):
        if user_guess == rand_word[i]:
            blank_spaces[i] = user_guess
    return blank_spaces


def is_wrong_guesses_equal_0(num_guesses):
    if num_guesses == 0:
        return True
    else:
        return False


def is_word_guessed(blank_spaces):
    for char in blank_spaces:
        if char == "_":
            return False
    return True


def print_win_or_lose(num_wrong_guesses):
    if num_wrong_guesses == 0:
        print("You Lose!")
    else:
        print("You Win!")


def play_word_game(rand_word, blank_spaces):
    num_wrong_guesses = 5
    print(f'This is for debugging purposes, and game testing: {rand_word}')
    while not is_wrong_guesses_equal_0(num_wrong_guesses) and not is_word_guessed(blank_spaces):
        blank_spaces_str = ''.join(blank_spaces)
        print(f'Guess the word: {blank_spaces_str}')
        user_guess = get_user_guess()
        print(f'You guessed {user_guess}\n')
        if is_user_guess_in_word(user_guess, rand_word):
            reveal_letter_in_word(user_guess, rand_word, blank_spaces)
        else:
            num_wrong_guesses -= 1
        print(f'You have {num_wrong_guesses} wrong guess(es) remaining.\n')
    print_win_or_lose(num_wrong_guesses)


def print_rand_word(rand_word):
    print(f'The word was {rand_word}!')
