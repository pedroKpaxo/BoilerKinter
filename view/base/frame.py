from tkinter.ttk import Frame


class GridFrame(Frame):
    """Simple frame with grid configuration"""

    def __init__(self, container,):
        super().__init__(container)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

# TODO - Complete this frame


class CleanFrame(Frame):
    """Clean frame"""

    def __init__(self, container,):
        super().__init__(container)


class ControllableFrame(CleanFrame):
    """Simple frame with controller entry configuration"""

    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller


class ControllableGridFrame(GridFrame):
    """Simple frame with controller entry configuration"""

    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
