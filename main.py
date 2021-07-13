from data_management import *
from ui import Menu

menu = Menu()
menu.start_programm()

# old_dict = load_learning_state('dictionary.pkl')
# new_dict = {}
# for k in list(old_dict.keys()):
#     old_entry = old_dict[k]
#     entry = Entry(k, old_dict[k].answer)
#     entry.num_right_guess = old_entry.num_right_guess
#     entry.num_close_guess = old_entry.num_close_guess
#     entry.num_wrong_guess = old_entry.num_wrong_guess
#     entry.update_rank()
#     new_dict[k] = entry
#
# save_learning_state_at(new_dict, 'new_dict.pkl')


# new_dict = load_learning_state('new_dict.pkl')
# print(new_dict[list(new_dict.keys())[0]].rank, new_dict[list(new_dict.keys())[0]].word)

