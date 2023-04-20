from abc import abstractmethod
from tkinter import Toplevel

from AAkinter.database.models.base_model import BaseModel
from AAkinter.view.themed_view import ThemedMapView

from .base import widget_config, ControllableFrame


class BoilerTopLevel(Toplevel):
    """
    Base for a tkinter.TopLevelit packs a MAIN frame inside itself.\n
    Override the MAIN class attribute with your frame of choice\n
    MAIN: class variable that defines a controllable frame object

    """

    MAIN = ControllableFrame
    main_frame: MAIN

    GEOMETRY = "1230x700"

    def __init__(self, master, controller):
        super().__init__(master,)
        self.controller = controller
        self.geometry(self.GEOMETRY)
        self.option_add('*tearOff', False)
        # - Defines a MAIN frame to be packed
        self.main_frame = self.MAIN(self, self.controller)

    def pack_main_frame(self):
        """Packs the main_frame attribute, running the TopLevel"""
        self.main_frame.pack(**widget_config.PACK_EXPAND)

    def destroy_self(self):
        self.destroy()

    def configure_info(self, model: BaseModel):
        pass


class TopLevelThemedView(BoilerTopLevel):

    MAIN = ThemedMapView

    def __init__(self, master, controller):
        super().__init__(master, controller)
