import tkinter as tk
from tkinter.ttk import *
from tkinter import scrolledtext

win = tk.Tk()

win.title('First Gui')

# win.resizable(False, False)


def click_me():
    button.configure(text='Hello ' + name.get() + 'you are ' + number.get())

button = Button(win, text='Click Me!', command=click_me)
button.grid(column=2, row=1)

Label(win, text='Enter a name:', justify='left').grid(column=0, row=0)
name = tk.StringVar()
name_entered = Entry(win, textvariable=name )
name_entered.configure(width=12)
name_entered.grid(column=0, row=1)
# name_entered.focus\9

Label(win, text='Choose a number:').grid(column=1, row=0)
number = tk.StringVar()
options = (1, 2, 4, 42, 100)
number_chosen = Combobox(win, width=12, textvariable=number, values=(1, 2, 4, 42, 100), state='readonly')
number_chosen.config(width=12)
number_chosen.grid(column=1, row=1)
number_chosen.current(1)

# Creating three checkbuttoons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text='Disabled', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=2, sticky=tk.W)

chVarUn = tk.IntVar()
check1 = tk.Checkbutton(win, text='Unchecked', variable=chVarUn )
check1.deselect()
check1.grid(column=1, row=2, sticky=tk.W)

chVarEn = tk.IntVar()
check1 = tk.Checkbutton(win, text='Enabled', variable='chVarEn')
check1.select()
check1.grid(column=2, row=2, sticky=tk.W)

# radio button Globals
colors = ['Blue', 'Red', 'Gold']

def radCall():
    radSel = radVar.get()
    if radSel == 0: win.configure(background=colors[0] )
    elif radSel == 1 : win.configure(background=colors[1])
    elif radSel == 2: win.configure(background=colors[2])

radVar = tk.IntVar()

for col in range(3):
    curRad = Radiobutton(win, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=3, sticky=tk.W)

scrol_w = 30 
scrol_h = 3
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

buttons_frame = LabelFrame(win, text= ' Labels in a frame ')
buttons_frame.grid(column=0, row=5)

Label(buttons_frame, text='Label 1').grid(column=0, row=0, sticky=tk.W)
Label(buttons_frame, text='Label 2').grid(column=1, row=0, sticky=tk.W)
Label(buttons_frame, text='Label 3').grid(column=2, row=0, sticky=tk.W)

win.mainloop()
