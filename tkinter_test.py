from tkinter import *
import random
from tkinter import scrolledtext


def func_test():
    pass


root = Tk()


# # # Creating tkinter scrolled text widget
# root.title("ScrolledText Widget")
# Label(root, text="ScrolledText Widget Example", font=("Times New Roman", 15), background='green',
#       foreground="white").grid(column=0, row=0)
#
# # Creating scrolled text area
# text_area = scrolledtext.ScrolledText(root, wrap=WORD, width=30, height=8, font=("Times New Roman", 15))
# text_area.grid(column=0, pady=10, padx=10)
#
# # Inserting Text which is read only
# text_area.insert(INSERT,
# """\
# This is a scrolledtext widget to make tkinter text read only.
# Hi
# Geeks !!!
# Geeks !!!
# Geeks !!!
# Geeks !!!
# Geeks !!!
# Geeks !!!
# Geeks !!!
# but if the state is not disabled, it will be editable :D
# """)
#
# read_only = True
# if read_only:
#     # Making the text read only by disabling the state
#     text_area.configure(state='disabled')
# else:
#     # Placing cursor in the text area for edit
#     text_area.focus()


# ### Place example
# # width x height + x_offset + y_offset:
# root.geometry("170x200+30+30")
#
# languages = ['PythonehbflUWEBFLUwebfuBEUFb', 'Perl', 'C++', 'Java', 'Tcl/Tk']
# labels = range(5)
# for i in range(5):
#     ct = [random.randrange(256) for x in range(3)]
#     brightness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
#     ct_hex = "%02x%02x%02x" % tuple(ct)
#     bg_colour = '#' + "".join(ct_hex)
#     l = Label(root,
#                  text=languages[i],
#                  fg='White' if brightness < 120 else 'Black',
#                  bg=bg_colour)
#     l.place(x=20, y=30 + i * 30, width=120, height=25)

# ### Learning interface
root.title('My own flashcards')
root.geometry('700x400')

btn_font_size = 12
learning_ui = []
cards_num = Label(root, text='001/100', font=('Arial', 12))
cards_num.grid(column=0, row=0)
word = Label(root, text='Wort', font=('Arial', 30))
word.grid(column=1, row=0)
# # Old answer text placeholder
# answer = Label(root, text='-----------------------------\n-------------------------------------', font=('Arial', 15))
# answer.grid(column=1, row=1)
# New answer text placeholder
answer = scrolledtext.ScrolledText(root, wrap=WORD, width=30, height=2, font=("Times New Roman", 15))
answer.grid(column=1, row=1, pady=20, padx=20)
answer.insert(INSERT, "This is a scrolledtext widget to make tkinter text read only. Hi, Geeks !!!\
                       but if the state is not disabled, it will be editable :D")
answer.delete('1.0', END)
answer.insert(INSERT, "This is new text")
# answer.focus()  # to make focus to this textbox
right_answer = Label(root, text='0', fg='green', font=('Arial', btn_font_size))
right_answer.grid(column=0, row=4)
close_answer = Label(root, text='0', fg='orange', font=('Arial', btn_font_size))
close_answer.grid(column=1, row=4)
wrong_answer = Label(root, text='0', fg='red', font=('Arial', btn_font_size))
wrong_answer.grid(column=2, row=4)

get_answer = Button(root, text='Antwort zeigen', fg='black', command=func_test(), font=('Arial', btn_font_size))
get_answer.grid(column=1, row=2)

btn_right = Button(root, text='Richtig!', fg='green', command=func_test, font=('Arial', btn_font_size))
btn_right.grid(column=0, row=3)
btn_close = Button(root, text='Teilweise', fg='orange', command=func_test, font=('Arial', btn_font_size))
btn_close.grid(column=1, row=3)
btn_wrong = Button(root, text='Unbekannt', fg='red', command=func_test, font=('Arial', btn_font_size))
btn_wrong.grid(column=2, row=3)

# ##### --- Menu ---
# learn_non_seen_btn = Button(root, text='Study non seen', fg='black', command=func_test, font=('Arial', 12))
# learn_non_seen_btn.grid(column=0, row=0)
#
# learn_all_btn = Button(root, text='Study most difficult', fg='black', command=func_test, font=('Arial', 12))
# learn_all_btn.grid(column=0, row=1)
#
# learn_all_btn = Button(root, text='Study partially learnt', fg='black', command=func_test, font=('Arial', 12))
# learn_all_btn.grid(column=0, row=2)
#
# learn_all_btn = Button(root, text='Study sorted', fg='black', command=func_test, font=('Arial', 12))
# learn_all_btn.grid(column=0, row=3)
#
# learn_all_btn = Button(root, text='Study all', fg='black', command=func_test, font=('Arial', 12))
# learn_all_btn.grid(column=0, row=4)

root.mainloop()

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
