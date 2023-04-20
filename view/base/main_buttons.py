from tkinter.ttk import Button
from .frame import GridFrame
from tkinter.constants import W, E, N, S


class ButtonFrameMaster(GridFrame):
    """Gried frame with 6 Buttons"""

    def __init__(self, container):
        super().__init__(container)

        self.btn_1 = Button(self, text="Button 1")
        self.btn_1.grid(row=0, column=1, sticky=W+E+N+S)

        self.btn_2 = Button(
            self, text="Button 2")
        self.btn_2.grid(row=1, column=1, sticky=W+E+N+S)

        self.btn_3 = Button(self, text="Button 3")
        self.btn_3.grid(row=2, column=1, sticky=W+E+N+S)

        self.btn_4 = Button(
            self, text="Button 4")
        self.btn_4.grid(row=3, column=1, sticky=W+E+N+S)

        self.btn_5 = Button(
            self, text="Button 5")
        self.btn_5.grid(row=4, column=1, sticky=W+E+N+S)

        self.btn_6 = Button(
            self, text="Button 6")
        self.btn_6.grid(row=5, column=1, sticky=W+E+N+S)
