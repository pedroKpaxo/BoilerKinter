from tkinter import ttk

from .Frames import MenuLeft,StatusBar,RightArea,ButtonFrameMaster
from ..Styles import PAD5

class Layout(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)

        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure(1,weight=1)

        self.MenuLeft = MenuLeft(self)
        self.RightArea = RightArea(self)
        self.StatusBar = StatusBar(self)

        self.MasterButtons = ButtonFrameMaster(self.MenuLeft.menu_left_upper)
        self.MasterButtons.pack()

        self.MenuLeft.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.RightArea.grid(row=0, column=1, sticky="ew")
        self.StatusBar.grid(row=2, column=0, columnspan=2, sticky="ew")


