from tkinter import *
from tkinter import scrolledtext
from data_management import *
import random


class Menu:
    def __init__(self):
        self.root = Tk()
        self.root.title('My own flashcards')
        self.root.geometry('700x400')
        self.learning_gui = None

        self.root.grid_columnconfigure(3, minsize=100)
        self.continue_btn = Button(self.root, text='Continue', fg='black', command=self.continue_learning,
                                   font=('Arial', 12))
        self.continue_btn.grid(column=0, row=0)

        self.update_dict_btn = Button(self.root, text='Update dictionary', fg='black', command=self.update_dictionary,
                                      font=('Arial', 12))
        self.update_dict_btn.grid(column=0, row=1)
        self.dictionary = None

    def continue_learning(self):  # Check if there is any dictionary to continue on
        self.delete_all_in_root()
        self.dictionary = load_learning_state('dictionary.pkl')
        self.learning_gui = GUI(self.dictionary, self.root)

    def update_dictionary(self):  # Check if there is any dictionary to work on
        old_dictionary = load_learning_state('dictionary.pkl')
        old_key_list = list(old_dictionary.keys())
        new_dictionary = get_dict_from_excl_at('../../wokabelheft_zu_importieren.xlsx')
        new_key_list = list(new_dictionary.keys())
        num_new_words = 0
        num_updated_words = 0
        for k in new_key_list:
            if k in old_key_list:
                update_entry = Entry(k, new_dictionary[k].answer)
                update_entry.num_right_guess = old_dictionary[k].num_right_guess
                update_entry.num_close_guess = old_dictionary[k].num_close_guess
                update_entry.num_wrong_guess = old_dictionary[k].num_wrong_guess
                old_dictionary[k] = update_entry
                num_updated_words += 1
            else:
                old_dictionary[k] = new_dictionary[k]
                num_new_words += 1
        save_learning_state_at(old_dictionary, 'dictionary.pkl')
        print('Dictionary Updated, {} words added, {} words updated'.format(num_new_words, num_updated_words))
        pass

    def delete_all_in_root(self):
        list_to_destroy = [x for x in self.root.children.values()]
        for label in list_to_destroy:
            label.destroy()

    def start_programm(self):
        self.root.mainloop()
        if self.dictionary is not None:
            save_learning_state_at(self.dictionary, 'dictionary.pkl')
            print('Learning process saved')
        else:
            print('Nothing to save')


class GUI:
    def __init__(self, dict_input, root):
        self.root = root
        self.dictionary = dict_input
        self.learning_interface = None
        self.learn_non_seen_btn = None
        self.learn_all_btn = None
        self.display_learning_menu()

    def display_learning_menu(self):
        self.delete_all_in_root()
        self.learn_non_seen_btn = Button(self.root, text='Study non seen', fg='black', command=self.learn_non_seen,
                                         font=('Arial', 12))
        self.learn_non_seen_btn.grid(column=0, row=0)

        self.learn_all_btn = Button(self.root, text='Study most difficult', fg='black', command=self.learn_difficult,
                                    font=('Arial', 12))
        self.learn_all_btn.grid(column=0, row=1)

        self.learn_all_btn = Button(self.root, text='Study partially learnt', fg='black', command=self.learn_partial,
                                    font=('Arial', 12))
        self.learn_all_btn.grid(column=0, row=2)

        self.learn_all_btn = Button(self.root, text='Study sorted', fg='black', command=self.learn_sorted,
                                    font=('Arial', 12))
        self.learn_all_btn.grid(column=0, row=3)

        self.learn_all_btn = Button(self.root, text='Study all', fg='black', command=self.learn_all,
                                    font=('Arial', 12))
        self.learn_all_btn.grid(column=0, row=4)

    def delete_all_in_root(self):
        list_to_destroy = [x for x in self.root.children.values()]
        for label in list_to_destroy:
            label.destroy()

    def learn_non_seen(self):
        self.delete_all_in_root()
        self.learning_interface = LearningScreen(self.root, self.dictionary)
        self.learning_interface.key_list = get_non_seen_keys(self.dictionary)
        if len(list(self.learning_interface.key_list)) == 0:
            print("Oups! Theres no non-seen cards... Returning to Main Menu")
            self.display_learning_menu()
        else:
            self.learning_interface.order_keys('random')
            self.learning_interface.start_ui()

    def learn_difficult(self):
        self.delete_all_in_root()
        self.learning_interface = LearningScreen(self.root, self.dictionary)
        self.learning_interface.key_list = get_difficult_keys(self.dictionary)
        if len(list(self.learning_interface.key_list)) == 0:
            print("Oups! Theres no difficult cards... Returning to Main Menu")
            self.display_learning_menu()
        else:
            self.learning_interface.order_keys('random')
            self.learning_interface.start_ui()

    def learn_partial(self):
        self.delete_all_in_root()
        self.learning_interface = LearningScreen(self.root, get_non_seen(self.dictionary))
        self.learning_interface.key_list = get_partial_keys(self.dictionary)
        if len(list(self.learning_interface.key_list)) == 0:
            print("Oups! Theres no partially learnt cards... Returning to Main Menu")
            self.display_learning_menu()
        else:
            self.learning_interface.order_keys('random')
            self.learning_interface.start_ui()

    def learn_sorted(self):
        self.delete_all_in_root()
        self.learning_interface = LearningScreen(self.root, self.dictionary)
        self.learning_interface.order_keys('difficult_first')
        self.learning_interface.start_ui()

    def learn_all(self):
        self.delete_all_in_root()
        self.learning_interface = LearningScreen(self.root, self.dictionary)
        self.learning_interface.order_keys('random')
        self.learning_interface.start_ui()


class LearningScreen:
    def __init__(self, root, learning_dictionary):
        self.root = root
        self.btn_font_size = 12
        self.learning_ui = []
        self.cards_num = Label(self.root, text='001/100', font=('Arial', 12))
        self.cards_num.grid(column=0, row=0)
        self.word = Label(self.root, text='Wort', font=('Arial', 30))
        self.word.grid(column=1, row=0)
        # self.answer = Label(self.root, text='-------', font=('Arial', 15))  # old word text box
        # self.answer.grid(column=1, row=1)
        self.answer = scrolledtext.ScrolledText(root, wrap=WORD, width=30, height=2, font=('Arial', 15))
        self.answer.grid(column=1, row=1, pady=20, padx=20)
        # self.answer.insert(INSERT, '-------')
        self.save_changes = Button(self.root, text='Änderungen\nspeichern', fg='black', command=self.save_changes,
                                   font=('Arial', self.btn_font_size))
        self.save_changes.grid(column=2, row=1)
        self.right_answer = Label(self.root, text='0', fg='green', font=('Arial', self.btn_font_size))
        self.right_answer.grid(column=0, row=4)
        self.close_answer = Label(self.root, text='0', fg='orange', font=('Arial', self.btn_font_size))
        self.close_answer.grid(column=1, row=4)
        self.wrong_answer = Label(self.root, text='0', fg='red', font=('Arial', self.btn_font_size))
        self.wrong_answer.grid(column=2, row=4)

        self.get_answer = Button(self.root, text='Antwort zeigen', fg='black', command=self.show_answer,
                                 font=('Arial', self.btn_font_size))
        self.get_answer.grid(column=1, row=2)

        self.btn_right = Button(self.root, text='Richtig!', fg='green', command=self.click_right,
                                font=('Arial', self.btn_font_size))
        self.btn_right.grid(column=0, row=3)
        self.btn_close = Button(self.root, text='Teilweise', fg='orange', command=self.click_close,
                                font=('Arial', self.btn_font_size))
        self.btn_close.grid(column=1, row=3)
        self.btn_wrong = Button(self.root, text='Unbekannt', fg='red', command=self.click_wrong,
                                font=('Arial', self.btn_font_size))
        self.btn_wrong.grid(column=2, row=3)

        self.dictionary = learning_dictionary
        self.key_list = list(self.dictionary.keys())
        self.key_id = 0

        self.start_ui()

        if __name__ == '__main__':
            self.key_list = self.key_list[:5]

    def order_keys(self, mode):
        if mode == 'random':
            random.shuffle(self.key_list)
        elif mode == 'difficult_first':
            for k in self.key_list:
                self.dictionary[k].update_rank()
            self.key_list.sort(key=lambda x: self.dictionary[x].rank, reverse=False)
            for k in self.key_list:
                print(k, self.dictionary[k].rank)
        else:
            pass

    def new_word(self):
        save_learning_state(self.dictionary)
        if self.key_id < len(self.key_list) - 1:
            self.key_id += 1
        else:
            self.key_id = 0
        self.cards_num.configure(text=str(self.key_id + 1) + '/' + str(len(self.key_list)))
        self.word.configure(text=self.key_list[self.key_id])
        # self.answer.configure(text='-------')  # old text box
        self.answer.delete('1.0', END)           # new text box
        self.right_answer.configure(text=str(self.dictionary[self.key_list[self.key_id]].num_right_guess))
        self.close_answer.configure(text=str(self.dictionary[self.key_list[self.key_id]].num_close_guess))
        self.wrong_answer.configure(text=str(self.dictionary[self.key_list[self.key_id]].num_wrong_guess))

    def show_answer(self):
        # self.answer.configure(text=self.dictionary[self.key_list[self.key_id]].answer)  # old answer box
        self.answer.delete('1.0', END)                                                    # new answer scroll box
        self.answer.insert(INSERT, self.dictionary[self.key_list[self.key_id]].answer)    # new answer scroll box

    def save_changes(self):
        pass

    def click_right(self):
        self.dictionary[self.key_list[self.key_id]].num_right_guess += 1
        self.new_word()

    def click_close(self):
        self.dictionary[self.key_list[self.key_id]].num_close_guess += 1
        self.new_word()

    def click_wrong(self):
        self.dictionary[self.key_list[self.key_id]].num_wrong_guess += 1
        self.new_word()

    def delete_learning_ui(self):
        for label in self.learning_ui:
            label.destroy()

    def delete_all_in_root(self):
        list_to_destroy = [x for x in self.root.children.values()]
        for label in list_to_destroy:
            label.destroy()

    def start_ui(self):
        self.cards_num.configure(text=str(self.key_id + 1) + '/' + str(len(self.key_list)))
        self.word.configure(text=self.key_list[self.key_id])
        self.right_answer.configure(text=str(self.dictionary[self.key_list[self.key_id]].num_right_guess))
        self.close_answer.configure(text=str(self.dictionary[self.key_list[self.key_id]].num_close_guess))
        self.wrong_answer.configure(text=str(self.dictionary[self.key_list[self.key_id]].num_wrong_guess))


if __name__ == '__main__':
    menu = Menu()
    menu.start_programm()
