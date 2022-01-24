from tkinter import ttk
from tkinter.constants import *


class ButtonFrameMaster(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.button1 = ttk.Button(self, text="Button 1", width=25)
        self.button1.grid(row=0, column=1, columnspan=2, sticky=W+E+N+S)

        self.button2 = ttk.Button(self, text="Button 2")
        self.button2.grid(row=1, column=1, sticky=W+E+N+S)

        self.button3 = ttk.Button(self, text="Button 3")
        self.button3.grid(row=1, column=2, sticky=W+E+N+S)

        self.button4 = ttk.Button(self, text="Button 4")
        self.button4.grid(row=2, column=1, columnspan=2, sticky=W+E+N+S)
