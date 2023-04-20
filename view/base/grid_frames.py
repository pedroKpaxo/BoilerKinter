from tkinter.ttk import Frame, Label


class DisplayArea(Frame):
    def __init__(self, container):
        super().__init__(container)

    def expand_pack(self):
        return self.pack(fill="both", expand=True)


class StatusBar(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.config(borderwidth=2, relief="groove")
        self.status = Label(self, text="", font=('Helvetica bold', 10))
        self.status.pack(fill="both", expand=True)
