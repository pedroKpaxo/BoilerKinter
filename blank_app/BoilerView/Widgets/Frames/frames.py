from tkinter import ttk


class MenuLeft(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)
        self.config(borderwidth=2, relief="groove")
        self.menu_left_upper = ttk.Frame(self, width=150, height=150)
        self.menu_left_lower = ttk.Frame(self, width=150)

        self.test = ttk.Label(self.menu_left_upper, text="Left Menu Area")
        self.test.pack()

        self.menu_left_upper.pack(side="top", fill="both", expand=True)
        self.menu_left_lower.pack(side="top", fill="both", expand=True)


class RightArea(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # right area
        self.some_title = ttk.Label(self, text="Right Area")
        self.some_title.pack()

        self.canvas_area = ttk.Frame(self, width=500, height=400)
        self.canvas_area.pack()


class StatusBar(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # status bar
        self.config(borderwidth=2, relief="groove")
        self.status = ttk.Label(self, text="this is the status bar")
        self.status.pack(fill="both", expand=True)
