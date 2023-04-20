from cgitb import text
from tkinter import PhotoImage
from tkinter.ttk import Button

from .frame import GridFrame, CleanFrame
from . import paddings, widget_config
from .constants import W, E, S, N


class HorizontalButtons(GridFrame):

    button_1: Button
    button_2: Button
    button_3: Button
    button_4: Button

    btn_1_text = ''
    btn_2_text = ''
    btn_3_text = ''
    btn_4_text = ''
    btn_5_text = ''
    btn_6_text = ''

    def __init__(self, container) -> None:
        super().__init__(container)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.config(borderwidth=1, relief="groove", padding=0)

        self.CONTAINER_0 = CleanFrame(self)
        self.button_0 = Button(self.CONTAINER_0, text='')
        self.button_0.pack(**widget_config.PACK_EXPANDX)
        self.CONTAINER_0.grid(row=1, column=1, sticky=W+E+N+S)  # noqa

        self.CONTAINER_1 = CleanFrame(self)
        self.button_1 = Button(self.CONTAINER_1, text=self.btn_1_text)
        self.button_1.pack(**widget_config.PACK_EXPANDX)
        self.CONTAINER_1.grid(row=1, column=2, sticky=W+E+N+S)  # noqa

        self.CONTAINER_2 = CleanFrame(self)
        self.button_2 = Button(self.CONTAINER_2, text=self.btn_2_text)
        self.button_2.pack(**widget_config.PACK_EXPANDX)
        self.CONTAINER_2.grid(row=1, column=3, sticky=W+E+N+S)  # noqa

        self.CONTAINER_3 = CleanFrame(self)
        self.button_3 = Button(self.CONTAINER_3, text=self.btn_3_text)
        self.button_3.pack(**widget_config.PACK_EXPANDX)
        self.CONTAINER_3.grid(row=1, column=4, sticky=W+E+N+S)  # noqa

        self.CONTAINER_4 = CleanFrame(self)
        self.button_4 = Button(self.CONTAINER_4, text=self.btn_4_text)
        self.button_4.pack(**widget_config.PACK_EXPANDX)
        self.CONTAINER_4.grid(row=1, column=5, sticky=W+E+N+S)  # noqa

        self.CONTAINER_5 = CleanFrame(self)
        self.button_5 = Button(self.CONTAINER_5, text=self.btn_5_text)
        self.button_5.pack(**widget_config.PACK_EXPANDX)
        self.CONTAINER_5.grid(row=1, column=6, sticky=W+E+N+S)  # noqa

        self.CONTAINER_6 = CleanFrame(self)
        self.button_6 = Button(self.CONTAINER_6, text=self.btn_6_text)
        self.button_6.pack(**widget_config.PACK_EXPANDX)
        self.CONTAINER_6.grid(row=1, column=7, sticky=W+E+N+S)  # noqa

    def set_names(self, tuple_config: list[(str, PhotoImage)] = [('', None)]) -> None:
        """Receives a tuple and sets the text and image of the buttons"""
        self.button_1.configure(text=tuple_config[0], image=tuple_config[1])
        self.button_2.configure(text=tuple_config[0], image=tuple_config[1])
        self.button_3.configure(text=tuple_config[0], image=tuple_config[1])
        self.button_4.configure(text=tuple_config[0], image=tuple_config[1])
        return
        # XXX Remove this shit after test
        self.button_1.configure(image=tuple_config[1])
        self.button_2.configure(image=tuple_config[1])
        self.button_3.configure(image=tuple_config[1])
        self.button_4.configure(image=tuple_config[1])
