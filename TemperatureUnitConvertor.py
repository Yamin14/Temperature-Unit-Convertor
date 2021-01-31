from tkinter import *
root = Tk()
bg = "green"
fg = "sky blue"
acbg = "pink"
root.config(background=bg)

frame = Frame(root, bg=bg)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def submit():
	fro = tkvar1.get()
	to = tkvar2.get()
	input = entry.get()
	if fro == to:
		result['text'] = input
	
	elif input == "":
		result['text'] = ""

	elif fro == 'Celsius':
		if to == 'Fahrenheit':
			res = (float(input) * 1.8) + 32
			result['text'] = str(res)
		elif to == 'Kelvin':
			res = float(input) + 273.15
			result['text'] = str(res)
			
	elif fro == 'Fahrenheit':
		if to == 'Celsius':
			res = (float(input) - 32) / 1.8
			result['text'] = str(res)
		elif to == 'Kelvin':
			res = (float(input) + 459.67) / 1.8
			result['text'] = str(res)
			
	elif fro == 'Kelvin':
		if to == 'Fahrenheit':
			res = (float(input) * 1.8) - 459.67
			result['text'] = str(res)
		elif to == 'Celsius':
			res = float(input) - 273.15
			result['text'] = str(res)

heading = Label(frame, text="Temperature Unit Convertor", bg=bg, fg=fg, font=("Comic Sans MS", 12, 'underline'))
heading.pack()

gridframe = Frame(frame, bg=bg)
gridframe.pack()

tkvar1 = StringVar()
options = ['Celsius', 'Fahrenheit', 'Kelvin']

from_menu = OptionMenu(gridframe, tkvar1, *options)
from_menu.config(bg=bg, activebackground=bg, fg=fg)
from_menu['menu'].config(bg=bg, activebackground=bg, fg=fg)
tkvar1.set("From")
from_menu.grid(row=0, column=0)

tkvar2 = StringVar()

to_menu = OptionMenu(gridframe, tkvar2, *options)
to_menu.config(bg=bg, activebackground=bg, fg=fg)
to_menu['menu'].config(bg=bg, activebackground=bg, fg=fg)
tkvar2.set("To")
to_menu.grid(row=0, column=1)

enter = Label(gridframe, text="Enter:  ", bg=bg, fg=fg, font=("Comic Sans MS", 7))
enter.grid(row=1, column=0)

entry = Entry(gridframe, width=12)
entry.grid(row=1, column=1)

result_text = Label(gridframe, text="Result: ", bg=bg, fg=fg, font=("Comic Sans MS", 7))
result_text.grid(row=2, column=0)

result = Label(gridframe, text="", bg=bg, fg="yellow", font=("Comic Sans MS", 14))
result.grid(row=2, column=1)

submitbtn = Button(frame, text="Submit", bg=fg, fg="#000055", activebackground=acbg, command=submit)
submitbtn.pack()

root.mainloop()
