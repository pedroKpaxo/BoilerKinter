from tkinter.ttk import Frame
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from AAkinter.view.base import widget_config

class CanvasFrame(Frame):

    figure = Figure()

    def __init__(self, master):
        super().__init__(master)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        #self.toolbar = NavigationToolbar2Tk(self.canvas, root)
        self.canvas.draw()
        self.canvas.mpl_connect("key_press_event", self.on_key_press)

    def pack_canvas(self):
        self.canvas.get_tk_widget().pack(**widget_config.PACK_EXPAND)
        # self.toolbar.update()

    def add_fig_subplot(self, __plot):
        self.canvas.figure.add_subplot(111).plot(__plot)

    def set_figure(self, fig: Figure):
        self.canvas.figure = fig
        self.canvas.draw()

    def on_key_press(self, event):
        print("you pressed {}".format(event.key))
        self.canvas.button_press_event(event, self.canvas, self.toolbar)