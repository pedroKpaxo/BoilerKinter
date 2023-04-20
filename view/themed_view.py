from typing import Any

from .base.constants import BOTH, END, LEFT, RIGHT
from .base import MapFrame, paddings
from .blocks import BlockFrame
from .creator_grids import ControllableDetailGrid


class ThemedMapView(ControllableDetailGrid):
    """
    Base class for themed views.\n
    The main objective is to be packed in a toplevel.\n
    """

    MAIN_THEME = ''
    HELP_TEXT_T_1_GN = '#############'
    HELP_TEXT_T_2_GN = '############'

    def __init__(self, master, controller):
        super().__init__(master, controller)
        self.config(borderwidth=2, relief="groove")
        # - Double Note
        self.block_1 = BlockFrame(self.display_area)
        self.block_1.configure(width=100)
        self.block_1.pack_propagate(0)
        self.block_1.notebook_general.tab(1, text=self.HELP_TEXT_T_1_GN)
        self.block_1.lower_notebook.tab(0, text='Lista de campos encontrados')
        self.block_1.pack(side=LEFT, expand=1, fill=BOTH, **paddings.PAD5Y15X)
        # - MAP
        self.block_2 = MapFrame(self.display_area)
        self.block_2.pack(side=RIGHT, expand=1, fill=BOTH, **paddings.PAD5Y15X)
        self.bind_motion()

    async def insert_rows_general_info(self, data: list[tuple[Any, Any]]):
        """
        Inserts rows in tree_2_notebook_general in 
         async manner, or at least try
        """
        for x in data:
            self.block_1.tree_1_notebook_general.insert(
                '', END, values=(x[0], x[1]))
        return

    async def insert_tree_2_notebook_general(self, data: list[tuple[Any, Any]]):
        """
        Inserts rows in tree_2_notebook_general in 
         async manner, or at least try
        """
        for x in data:
            self.block_1.tree_2_notebook_general.insert(
                '', END, values=(x[0], x[1]))
        return

    async def insert_tree_1_lower_notebook(self, data: list[tuple[Any, Any]]):
        """
        Inserts rows in tree_1_lower_notebook in 
         async manner, or at least try
        """
        for x in data:
            self.block_1.tree_1_lower_notebook.insert(
                '', END, values=(x[0], x[1]), iid=x)
        return

    def bind_motion(self):
        """
        Binds text to be displayed
        in the status_bar when the mouse enters
        this widget
        """
        # - Binding tree 1 of the general notebook
        self.block_1.tree_1_notebook_general.bind(
            '<Motion>', self.motion__general_info_table)
        # - Binding tree 2 of the general notebook
        self.block_1.tree_2_notebook_general.bind(
            '<Motion>', self.motion__genral_info_table_2)
        self.block_2.map.bind(
            '<Motion>', self.motion_map_frame)

    def motion__general_info_table(self, event):
        """
        Binds text to be displayed
        in the status_bar when the mouse enters
        this widget
        """
        self.status_bar.status.config(
            text=self.HELP_TEXT_T_1_GN)

    def motion__genral_info_table_2(self, event):
        """
        Binds text to be displayed
        in the status_bar when the mouse enters
        this widget
        """
        self.status_bar.status.config(
            text=self.HELP_TEXT_T_1_GN)

    def motion_map_frame(self, event):
        """
        Binds text to be displayed
        in the status_bar when the mouse enters
        this widget
        """
        self.status_bar.status.config(
            text=self.HELP_TEXT_T_2_GN)

    def configure_info(self):
        pass


