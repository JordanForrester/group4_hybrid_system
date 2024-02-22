
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
from tkinter.ttk import Treeview
from PIL import Image, ImageTk
import tkinter.font
from tkinter import filedialog




class Widget1():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.configure(bg = '#414141')
            self.w1.geometry('1280x720')
        else:
            self.w1 = Frame(parent)
            self.w1.configure(bg = '#414141')
            self.w1.place(x = 0, y = 0, width = 1280, height = 720)
        self.button1 = Button(self.w1, text = "Search", font = tkinter.font.Font(family = "Verdana", size = 12), cursor = "arrow", state = "normal")
        self.button1.place(x = 800, y = 50, width = 200, height = 40)
        self.button1['command'] = self.print_test
        self.text1 = Text(self.w1, font = tkinter.font.Font(family = "Verdana", size = 12), cursor = "arrow", state = "normal")
        self.text1.place(x = 300, y = 230, width = 400, height = 470)
        self.ltext1 = Entry(self.w1, font = tkinter.font.Font(family = "Verdana", size = 12), state = "normal")
        self.ltext1.place(x = 170, y = 50, width = 200, height = 40)
        self.label1 = Label(self.w1, text = "Keyword:", anchor='w', font = tkinter.font.Font(family = "Verdana", size = 12), cursor = "arrow", state = "normal")
        self.label1.place(x = 50, y = 50, width = 120, height = 40)
        self.button2 = Button(self.w1, text = "Directory Selector", font = tkinter.font.Font(family = "Verdana", size = 12), cursor = "arrow", state = "normal")
        self.button2.place(x = 500, y = 50, width = 200, height = 40)
        self.button2['command'] = self.browse_folder
        self.label2 = Label(self.w1, text = "Search Type", anchor='w', font = tkinter.font.Font(family = "Verdana", size = 12), cursor = "arrow", state = "normal")
        self.label2.place(x = 50, y = 160, width = 150, height = 22)
        self.combo1 = Combobox(self.w1, font = tkinter.font.Font(family = "Verdana", size = 12), cursor = "arrow", state = "normal")
        self.combo1.place(x = 50, y = 210, width = 160, height = 30)
        self.combo1['values'] = ("Disk & Gmail", "Disk Only", "Gmail only")
        self.combo1.current(0)
        self.label3 = Label(self.w1, text = "Selected Option", anchor='w', font = tkinter.font.Font(family = "Verdana", size = 12), cursor = "arrow", state = "normal")
        self.label3.place(x = 800, y = 170, width = 200, height = 22)
        self.label4 = Label(self.w1, text = "Search Results", anchor='w', font = tkinter.font.Font(family = "Verdana", size = 12), cursor = "arrow", state = "normal")
        self.label4.place(x = 300, y = 170, width = 200, height = 22)
        self.text3 = Text(self.w1, font = tkinter.font.Font(family = "Verdana", size = 12), cursor = "arrow", state = "normal")
        self.text3.place(x = 800, y = 230, width = 400, height = 470)

    def print_test(self):
        input = self.ltext1.get()
        print(input)

    def browse_folder(self):
        # Ask for text input from the user
        root = Tk()
        root.withdraw()  # Remove or comment out this line to keep the window visible
        folder_selected = filedialog.askdirectory()
        root.destroy()  # Close the Tkinter window after selecting the directory

if __name__ == '__main__':
    a = Widget1(0)
    a.w1.mainloop()