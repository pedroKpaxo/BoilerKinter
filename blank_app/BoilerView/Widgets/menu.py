from tkinter import Menu, Tk



class TopMenu(Menu):
    def __init__(self, container: Tk):
        super().__init__(container)
        
        # - Start a Menu Bar
        self.master = container
        # - add a filemenu to the menu bar
        self.file_menu = Menu(self)
        self.file_menu.add_command(
            label='Exit', command=self.master.destroy)
        self.add_cascade(
            label="File", menu=self.file_menu, underline=0)