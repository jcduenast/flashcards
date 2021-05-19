from tkinter import *
from data_management import *
import random


class GUI:
	def __init__(self, dict_input):
		self.root = Tk()
		self.root.title('My own flashcards with juegos de azar and mujerzuelas')
		self.root.geometry('700x400')
		self.root.grid_columnconfigure(3, minsize=100)
		self.dictionary = dict_input
		self.learning_interface = None

		self.learn_non_seen_btn = Button(self.root, text='Study non seen', fg='black', command=self.learn_non_seen,
								   font=('Arial', 12))
		self.learn_non_seen_btn.grid(column=0, row=0)

		self.learn_all_btn = Button(self.root, text='Study all', fg='black', command=self.learn_all,
								   font=('Arial', 12))
		self.learn_all_btn.grid(column=0, row=1)

	def delete_all_in_root(self):
		list_to_destroy = [x for x in self.root.children.values()]
		for label in list_to_destroy:
			label.destroy()

	def learn_non_seen(self):
		self.delete_all_in_root()
		self.learning_interface = LearningScreen(self.root, get_non_seen(self.dictionary))
		self.learning_interface.start_ui()

	def learn_all(self):
		self.delete_all_in_root()
		self.learning_interface = LearningScreen(self.root, self.dictionary)
		self.learning_interface.start_ui()

	def start_ui(self):
		self.root.mainloop()


class LearningScreen:
	def __init__(self, root, learning_dictionary):
		self.root = root
		self.btn_font_size = 12
		self.learning_ui = []
		self.cards_num = Label(self.root, text='001/100', font=('Arial', 12))
		self.cards_num.grid(column=0, row=0)
		self.word = Label(self.root, text='Wort', font=('Arial', 30))
		self.word.grid(column=1, row=0)
		self.answer = Label(self.root, text='-------', font=('Arial', 15))
		self.answer.grid(column=1, row=1)
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
		random.shuffle(self.key_list)
		self.key_id = 0

		self.start_ui()

		if __name__ == '__main__':
			self.key_list = self.key_list[:5]

	def new_word(self):
		if self.key_id < len(self.key_list) - 1:
			self.key_id += 1
		else:
			self.key_id = 0
		self.cards_num.configure(text=str(self.key_id + 1) + '/' + str(len(self.key_list)))
		self.word.configure(text=self.key_list[self.key_id])
		self.answer.configure(text='-------')
		self.right_answer.configure(text=str(self.dictionary[self.key_list[self.key_id]].num_right_guess))
		self.close_answer.configure(text=str(self.dictionary[self.key_list[self.key_id]].num_close_guess))
		self.wrong_answer.configure(text=str(self.dictionary[self.key_list[self.key_id]].num_wrong_guess))

	def show_answer(self):
		self.answer.configure(text=self.dictionary[self.key_list[self.key_id]].answer)

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
	dictionary = get_default()
	gui = GUI(dictionary)
	gui.start_ui()

# # create root window
# root = Tk()
#
# # root window title and dimension
# root.title("Welcome to GeekForGeeks")
# # Set geometry(widthxheight)
# root.geometry('350x200')
#
# # adding menu bar in root window
# # new item in menu bar labelled as 'New'
# # adding more items in the menu bar
# menu = Menu(root)
# item = Menu(menu)
# item.add_command(label='New')
# menu.add_cascade(label='File', menu=item)
# root.config(menu=menu)
#
# # adding a label to the root window
# lbl = Label(root, text = "Are you a Geek?")
# lbl.grid()
#
# # adding Entry Field
# txt = Entry(root, width=10)
# txt.grid(column =1, row =0)
#
#
# # function to display user text when
# # button is clicked
# def clicked():
#
# 	res = "You wrote" + txt.get()
# 	lbl.configure(text = res)
#
# # button widget with red color text inside
# btn = Button(root, text = "Click me" ,
# 			fg = "red", command=clicked)
# # Set Button Grid
# btn.grid(column=2, row=0)
#
# # Execute Tkinter
# root.mainloop()
