import tkinter as tk
from tkinter.ttk import *
from fileOrganizer import sort

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
dirEntry.insert(0, "'e.g: C:/Users/hp/Downloads'")
dirEntry.configure(font=('Courier', 15), state='disabled')


def clear(event):
    dirEntry.delete(0, 'end')
    dirEntry.configure(state='normal')


dirEntry.bind('<Button-1>', clear)

# file extentions to be sorted
file_ext = ['.txt', '.pdf', '.jpg', '.png', '.mp3', '.mp4', '.mkv', '.cdr',
            '.docx', '.ai', 'psd', '.py', '.html', '.js', '.svg', '.css', '.java', '.json']


chk_frame = LabelFrame(window, text=' specify file extentions ', width=100)
chk_frame.grid(column=0, row=2, sticky=tk.W, padx=20, columnspan=2)


ext_dict = {1: '.txt', 2: '.pdf', 3: '.jpg', 4: '.png', 5: '.mp3', 6: '.mp4', 7: '.mkv', 8: '.cdr', 9: '.docx',
    10: '.ai', 11: 'psd', 12: '.py', 13: '.html', 14: '.js', 15: '.svg', 16: '.css', 17: '.java', 18: '.json'}

# var = [tk.IntVar() for i in range(18)]
variables = []

for i in range(len(ext_dict.keys())):
    variables.append(tk.StringVar(value=ext_dict[i+1]))

ch_var1, ch_var2, ch_var3, ch_var4, ch_var5, ch_var6, ch_var7, ch_var8, ch_var9, ch_var10, ch_var11, ch_var12, ch_var13, ch_var14, ch_var15, ch_var16, ch_var17, ch_var18 = variables
variables_keys = [ch_var1, ch_var2, ch_var3, ch_var4, ch_var5, ch_var6, ch_var7, ch_var8, ch_var9,
    ch_var10, ch_var11, ch_var12, ch_var13, ch_var14, ch_var15, ch_var16, ch_var17, ch_var18]


def get_input():
    directory = entryVar.get()
    print(directory)
    file_extentions = []
    folders = []
    global variables_keys, file_ext
    if variables_keys[0].get() == file_ext[0]:
        file_extentions.append(file_ext[0])
        folders.append('txt_folder')
    if variables_keys[1].get() == file_ext[1]:
        file_extentions.append(file_ext[1])
        folders.append('pdf_folder')
    if variables_keys[2].get() == file_ext[2]:
        file_extentions.append(file_ext[2])
        folders.append('jpg_folder')
    if variables_keys[3].get() == file_ext[3]:
        file_extentions.append(file_ext[3])
        folders.append('png_folder')
    if variables_keys[4].get() == file_ext[4]:
        file_extentions.append(file_ext[4])
        folders.append('mp3_folder')
    if variables_keys[5].get() == file_ext[5]:
        file_extentions.append(file_ext[5])
        folders.append('mp4_folder')
    if variables_keys[6].get() == file_ext[6]:
        file_extentions.append(file_ext[6])
        folders.append('mkv_folder')
    if variables_keys[7].get() == file_ext[7]:
        file_extentions.append(file_ext[7])
        folders.append('cdr_folder')
    if variables_keys[8].get() == file_ext[8]:
        file_extentions.append(file_ext[8])
        folders.append('docx_folder')
    if variables_keys[9].get() == file_ext[9]:
        file_extentions.append(file_ext[9])
        folders.append('ai_folder')
    if variables_keys[10].get() == file_ext[10]:
        file_extentions.append(file_ext[10])
        folders.append('psd_folder')
    if variables_keys[11].get() == file_ext[11]:
        file_extentions.append(file_ext[11])
        folders.append('py_folder')
    if variables_keys[12].get() == file_ext[12]:
        file_extentions.append(file_ext[12])
        folders.append('html_folder')
    if variables_keys[13].get() == file_ext[13]:
        file_extentions.append(file_ext[13])
        folders.append('js_folder')
    if variables_keys[14].get() == file_ext[14]:
        file_extentions.append(file_ext[14])
        folders.append('svg_folder')
    if variables_keys[15].get() == file_ext[15]:
        file_extentions.append(file_ext[15])
        folders.append('css_folder')
    if variables_keys[16].get() == file_ext[16]:
        file_extentions.append(file_ext[16])
        folders.append('java_folder')
    if variables_keys[17].get() == file_ext[17]:
        file_extentions.append(file_ext[17])
        folders.append('json_folder')
    sort(directory, folders, file_extentions)

    
    

Button(window, width=20, text='Sort', command=get_input).grid(column=1, row=1, ipady=5)

for i in range(len(file_ext)):
    file_chk = Checkbutton(chk_frame, text=file_ext[i], variable=variables_keys[i], offvalue=0, onvalue=ext_dict[i+1])
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
