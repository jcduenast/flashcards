from tkinter import *
from data_management import get_default


class GUI:
	def __init__(self, dict_input):
		self.root = Tk()
		self.root.title('My own flashcards with juegos de azar and mujerzuelas')
		self.root.geometry('500x200')
		# self.root.grid_columnconfigure(3, minsize=100)
		self.root.option_add('*Font', '32')

		self.word = Label(self.root, text='Wort')
		self.word.grid(column=1, row=0)
		self.answer = Label(self.root, text='-------')
		self.answer.grid(column=1, row=1)
		self.right_answer = Label(self.root, text='0', fg='green')
		self.right_answer.grid(column=0, row=4)
		self.close_answer = Label(self.root, text='0', fg='orange')
		self.close_answer.grid(column=1, row=4)
		self.wrong_answer = Label(self.root, text='0', fg='red')
		self.wrong_answer.grid(column=2, row=4)

		self.get_answer = Button(self.root, text='Antwort zeigen', fg='black', command=self.show_answer)
		self.get_answer.grid(column=1, row=2)

		self.btn_right = Button(self.root, text='Richtig! :D', fg='green', command=self.click_right)
		self.btn_right.grid(column=0, row=3)
		self.btn_close = Button(self.root, text='Teilweise :s', fg='orange', command=self.click_close)
		self.btn_close.grid(column=1, row=3)
		self.btn_wrong = Button(self.root, text='Unbekannt :c', fg='red', command=self.click_wrong)
		self.btn_wrong.grid(column=2, row=3)
		self.dictionary = dict_input
		self.key_list = list(dict_input.keys())
		self.key_id = 0

		if __name__ == '__main__':
			self.key_list = list(dict_input.keys())[:5]

		# self.label = Label(self.root, text="Hello World")
		# self.label.pack(padx=5, pady=5)

	def new_word(self):
		if self.key_id < len(self.key_list)-1:
			self.key_id += 1
		else:
			self.key_id = 0
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

	def start_ui(self):
		self.word.configure(text=self.key_list[self.key_id])
		self.right_answer.configure(text=str(self.dictionary[self.key_list[self.key_id]].num_right_guess))
		self.close_answer.configure(text=str(self.dictionary[self.key_list[self.key_id]].num_close_guess))
		self.wrong_answer.configure(text=str(self.dictionary[self.key_list[self.key_id]].num_wrong_guess))
		self.root.mainloop()


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
