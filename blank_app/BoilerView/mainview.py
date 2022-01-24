import tkinter as tk
from .Widgets import TopMenu
from .Widgets import Layout

class App:

    def setup(self, controller):
        """
        Starting the main object tk.TK
        """

        self.controller = controller
        self.MainApp = tk.Tk()
        self.MainApp.title('Boiler Kinter by Pedro cavalcanti')
        # - Set the grid layout of the main TK object.
        self.MainApp.grid_rowconfigure(1, weight=1)
        self.MainApp.grid_columnconfigure(1, weight=1,)
        # - Set the size of the main object.
        self.MainApp.geometry("1230x700")
        self.MainApp.option_add('*tearOff', False)
        # - Start a Menu Bar
        self.MenuBar = TopMenu(self.MainApp)
        self.MainApp['menu'] = self.MenuBar
        
        self.createWidgets()

    def createWidgets(self):
        """
        This function allows you to create all the widgetes and pack them in the self.MainApp element.
        """
        self.layout = Layout(self.MainApp)
        self.layout.pack(expand=True,fill= tk.BOTH)
        

    def loop(self):
        self.MainApp.mainloop()
