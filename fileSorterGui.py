import shutil
import typing
import tkinter as tk
from tkinter.ttk import *
from pathlib import Path


class Sorter(tk.Frame):

    files = ["txt", "pdf", "jpg", "py", "mp3", "mp4", "html", "java",
             "ai", "psd", "cdr", "png", "csv", "js", "svg", "css", "json", "zip", "gif", "mov", "go", ]

    def __init__(self, master):
        super().__init__(master)
        self.window: tk.Tk = master
        self.window.title("File Sorter")
        self.window.geometry("600x300+350+250")
        self.window.resizable(False, False)
        self.variables()
        self.widgets()

    def variables(self):
        self.getEntry = tk.StringVar()
        self.varKeys = []
        for i in range(len(self.files)):
            self.varKeys.append(tk.BooleanVar(value=0))

    def widgets(self):
        Label(self.window, text="Enter a directory:").grid(
            column=0, row=0, sticky=tk.W, padx=20, pady=12)
        self.dirEntry = Entry(
            self.window, textvariable=self.getEntry, width=30)
        self.dirEntry.configure(font=("Courier", 15))
        self.dirEntry.grid(column=0, row=1, padx=20, pady=5, ipady=5)
        self.dirEntry.insert(0, "'e.g: Enter a directory'")
        self.dirEntry.bind(
            '<Button-1>', lambda event: self.dirEntry.delete(0, "end"))

        Button(self.window, width=20, text="Sort",
               command=self.sortFiles).grid(column=1, row=1, ipady=5)

        self.checkButtonsFrame = LabelFrame(
            self.window, text=" choose files to sort")
        self.checkButtonsFrame.grid(
            column=0, row=2, columnspan=2, sticky=tk.W, padx=20)

        col = 0
        row = 0
        for i in range(len(self.files)):
            if col % 10 == 0:
                col = 0
                row += 1
            fileChk = Checkbutton(
                self.checkButtonsFrame, text=self.files[i], variable=self.varKeys[i], offvalue=0, onvalue=1)
            fileChk.grid(column=col, row=row, sticky=tk.W, padx=5)
            col += 1

    def sortFiles(self):
        directory = self.getEntry.get()
        directory = Path(directory)
        try:
            assert directory.is_dir()
        except:
            pass
        else:
            filesToSort = []
            for i in range(len(self.files)):
                if self.varKeys[i].get():
                    filesToSort.append(self.files[i])
            sort(directory, filesToSort)


def sort(directory: Path, file_ext):
    for i in range(len(file_ext)):
        try:
            print(file_ext[i])
            newFolder = (directory / f"{file_ext[i]}_folder")
            newFolder.mkdir()
        except FileExistsError:
            pass

        for f in directory.glob(f'*.{file_ext[i]}'):
            shutil.move(f"{f}", newFolder)


if __name__ == "__main__":
    master = tk.Tk()
    sorter = Sorter(master)
    sorter.mainloop()
