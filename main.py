from create_word_bank import *
from word_game_setup import *
from word_game_logic import *

# get request from the website and create a word list
request = get_request_from_web()
bs4_object = create_bs4_object(request)
word_list = create_word_list(bs4_object)
word_list_stripped = strip_word_list(word_list)

# check if the project directory has a word bank xlsx
word_bank_exists = does_word_bank_exist()
create_word_bank(word_bank_exists, word_list_stripped)

# Setup the word game
print_title_statement()
print_game_rules()
wb_sheet = load_workbook()
# rand_word = select_random_word(wb_sheet)
rand_word = "ALL"
blank_spaces = get_blank_spaces(rand_word)

# play the game - handles the game loop until win or lose condition
blank_spaces_str = ''.join(blank_spaces)
print(f'Guess the word: {blank_spaces_str}')
user_guess = get_user_guess()
print(f'You guessed {user_guess}')
is_user_guess_in_word(user_guess, rand_word)
blank_spaces = reveal_letter_in_word(user_guess, rand_word, blank_spaces)
print(f'Guess the word: {blank_spaces}')
