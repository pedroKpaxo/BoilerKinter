
from tkinter.ttk import Label

from .base import paddings
from .base.frame import CleanFrame


class DoubleLabel(CleanFrame):

    BIG = ('Helvetiva bold', 15)
    SUB = ('Helvetiva bold', 11)

    def __init__(self, container):
        super().__init__(container)
        self.main_label = Label(self, text='', font=self.BIG)
        self.main_label.pack(**paddings.PAD5)
        self.sub_label = Label(self, text='', font=self.SUB)
        self.sub_label.pack(**paddings.PAD5)
