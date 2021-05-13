from data_management import *
import ui

dictionary = get_default()
save_learning_state(dictionary)

dictionary_loaded = load_learning_state('dictionary.pkl')
for key in dictionary_loaded.keys():
    print(dictionary_loaded[key].answer)

print('main, this is just a test')
