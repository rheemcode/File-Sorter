import tkinter as tk
from tkinter.ttk import *
from pathlib import Path

# creating a window
window = tk.Tk()
window.title("File Sorter")
window.geometry("600x300+350+250")
window.resizable(False, False)


# creating user input
entryVar = tk.StringVar()
Label(window, text="Enter a directory:", font=(None, 17)).grid(column=0, row=0, sticky=tk.W, padx=20, pady=12)
dirEntry = Entry(window, textvariable=entryVar, width=30)
dirEntry.grid(column=0, row=1, padx=20, pady=5, sticky=tk.W, ipady=5)
dirEntry.configure(font=('Courier', 15))

def get_input():
    directory = entryVar.get()
    directory = Path(directory)
    print(Path.is_dir(directory))
    

Button(window, width=20, text='Sort', command=get_input).grid(column=1, row=1, ipady=5)

# file extentions to be sorted 
file_ext = ['.txt', '.pdf', '.jpg', '.png', '.mp3', '.mp4', '.mkv', '.cdr',  '.docx', '.ai', 'psd', '.py', '.html', '.js', '.svg', '.css', '.java', '.json']


chk_frame = LabelFrame(window, text=' specify file extentions ', width=100)
chk_frame.grid(column=0, row=2, sticky=tk.W, padx=20, columnspan=2)

def check():
    isCheck = fileVal.get()
    if isCheck == 1:
        pass


fileVal = tk.IntVar()
for i in range(len(file_ext)):
    file_chk = Checkbutton(chk_frame, text=file_ext[i], variable="", command=check)
    file_chk.grid(column=i, row=0, sticky=tk.W)

child_list = []
for child in chk_frame.winfo_children():
    child.grid_configure(padx=5)
    child_list.append(child)

num = 0
for arrange in range(len(child_list)):
    if (arrange + 1) >= 10:
        child_list[arrange].grid_configure(column=num, row=2)
        num += 1

# main window loop
window.mainloop()
