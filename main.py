from data_management import *
from ui import GUI

dictionary = get_default()
save_learning_state(dictionary)

dictionary_loaded = load_learning_state('dictionary.pkl')
gui = GUI(dictionary_loaded)
gui.start_ui()
save_learning_state(dictionary_loaded)
