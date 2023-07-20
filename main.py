import create_word_bank
from create_word_bank import *

# get request from the website and create a word list
request = get_request_from_web()
bs4_object = create_bs4_object(request)
word_list = create_word_list(bs4_object)
word_list_stripped = strip_word_list(word_list)

# check if the project directory has a word bank xlsx
word_bank_exists = does_word_bank_exist()
create_word_bank(word_bank_exists, word_list_stripped)
print()
