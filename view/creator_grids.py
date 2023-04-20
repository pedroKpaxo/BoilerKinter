from .base import BoilerFrame, ControllableFrame
from .grids import NoMenuGrid

PACK_EXPAND_15x_5y = {"expand": True, "fill": 'both',
                      "fill": 'both', 'padx': 15, 'pady': 5}


class NoMenuGridCreator(NoMenuGrid, BoilerFrame):
    """
    A grid frame detail view, with status bar and main area.
    With no menu on the left.
    """

    def __init__(self, container):
        super().__init__(container)


class ControllableDetailGrid(ControllableFrame, NoMenuGridCreator):
    """A controllable detai view, with status bar and main area"""

    def __init__(self, master, controller):
        super().__init__(master, controller)
