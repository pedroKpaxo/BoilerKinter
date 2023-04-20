from tkinter.ttk import Frame
from .base import GridFrame

from .base.grid_frames import DisplayArea, StatusBar


class DefaultGridLayout(GridFrame):
    """
    A default grid layout.  \n
    It expands a plain grid grame into a layout grid \n
    It contains a menu in the left, a display area, and a status bar.\n
    \n
    #### $ menu_left, % display_area, = status_bar \n
    \n
    ###     $$ %%%%%%\n
    ###     $$ %%%%%%\n
    ###     ===========\n
    """

    MENU_TYPE = Frame
    menu_left: MENU_TYPE

    PAD = 0
    PAD_CONF = {"padx": PAD, "pady": PAD}

    def __init__(self, container):
        super().__init__(container)

    def pack_menu(self):
        self.menu_left = self.MENU_TYPE(self)
        self.menu_left.grid(row=0, column=0, rowspan=2, sticky="nsew", **self.PAD_CONF)  # noqa

    def pack_display(self):
        self.display_area = DisplayArea(self)
        self.display_area.grid(row=0, column=1, rowspan=2, sticky="nsew", **self.PAD_CONF)  # noqa

    def pack_status_bar(self):
        self.status_bar = StatusBar(self)
        self.status_bar.grid(row=2, column=0, columnspan=2, sticky="ew", **self.PAD_CONF)  # noqa


class NoMenuGrid(GridFrame):
    """
    A default grid layout. with no menu \n
    % display_area          \n
    = status_bar            \n
                            \n
    %%%%%%%%%               \n
    %%%%%%%%%               \n
    =========               \n
    """

    def __init__(self, container,):
        super().__init__(container)
        self.display_area = DisplayArea(self)
        self.status_bar = StatusBar(self)

        self.display_area.grid(row=0, column=0,
                               columnspan=2, rowspan=2,
                               sticky="nsew")

        self.status_bar.grid(row=2, column=0, columnspan=2, sticky="ew")
