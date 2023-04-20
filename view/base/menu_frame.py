

from tkinter.ttk import Frame, Separator

from .main_buttons import ButtonFrameMaster


class MenuLeft(Frame):

    UPPER_BUTTONS = ButtonFrameMaster
    menu_buttons: UPPER_BUTTONS

    def __init__(self, container):
        super().__init__(container)
        self.config(borderwidth=2, relief="groove")
        self.upper_frame = Frame(self)
        self.menu_buttons = self.UPPER_BUTTONS(self.upper_frame)
        self.menu_buttons.pack(side='top', fill="x", expand=True)
        self.upper_frame.pack(side="top", fill="x")
        self.separator = Separator(self)
        self.separator.pack(fill="x", expand=True)
        self.lower_frame = Frame(self, width=150)
        self.lower_frame.pack(side="bottom", fill="both", expand=True)
