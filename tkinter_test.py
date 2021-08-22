from tkinter import *
import random
from tkinter import scrolledtext


def func_test():
    pass


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
        self.answer = scrolledtext.ScrolledText(root, wrap=WORD, width=30, height=2, font=("Times New Roman", 15))
        self.answer.grid(column=1, row=1, pady=20, padx=20)
        # self.answer.insert(INSERT, '-------')
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
        pass
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


root = Tk()
gui_test = LearningScreen(root, {})
gui_test.start_ui()
root.mainloop()
