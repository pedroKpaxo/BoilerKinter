from abc import ABC, abstractmethod
from tkinter import Tk

from .base.frame import GridFrame
from .grids import DefaultGridLayout

class AbstractTkApp(ABC):

    layout_class = GridFrame
    main_app: Tk

    def setup(self, controller):
        """
        Starting the main object tk.TK
        """
        self.controller = controller
        self.main_app = Tk()
        self.main_app.title('Boiler APP')
        self.main_app.geometry("1230x700")
        self.main_app.option_add('*tearOff', False)
        self.set_layout(self.layout_class)

    @abstractmethod
    def set_layout(self, _type):
        """
        Pack your widgets here. Start with a frame or a layout manager object.
        """
        pass

class AbstractBoilerAPP:

    layout_class = GridFrame
    main_app: Tk

    def setup(self, controller):
        """
        Starting the main object tk.TK
        """
        self.controller = controller
        self.main_app = Tk()
        self.main_app.title('Boiler APP')
        self.main_app.geometry("1230x700")
        self.main_app.option_add('*tearOff', False)
        self.set_layout(self.layout_class)

    def set_layout(self, _type):
        """
        This function allows you to create all the widgetes and pack them in the self.main_app element.
        """
        self.layout = _type(self.main_app, status=self.status,
                            controller=self.controller, app_soul=self)
        self.layout.pack(expand=True, fill='both')

    def loop(self):
        self.main_app.mainloop()


class BoilerGridLayoutApp:

    layout_class: DefaultGridLayout
    main_app: Tk

    def __init__(self) -> None:
        self.status = None
        pass

    def setup(self, controller):
        """
        Starting the main object tk.TK
        """
        self.controller = controller
        self.main_app = Tk()
        self.main_app.title('Boiler APP')
        self.main_app.geometry("1230x700")
        self.main_app.option_add('*tearOff', False)
        self.set_layout(DefaultGridLayout)

    def set_layout(self, type=DefaultGridLayout):
        """
        This function allows you to create all the widgetes and pack them in the self.main_app element.
        """
        
        self.layout = type(self.main_app,
                           status=self.status,
                           controller=self.controller,
                           app_soul=self)
        self.layout.pack(expand=True, fill='both')

    def loop(self):
        self.main_app.mainloop()
