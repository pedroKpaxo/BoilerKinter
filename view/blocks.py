from tkinter.ttk import Frame
from .base import widget_config
from .base import HorizontalButtons
from .base import BoilerFrame
from .tags import DoubleLabel

PACK_EXPAND_15x_5y = {"expand": True, "fill": 'both', 'padx': 15, 'pady': 5}
PACK_EXPAND = {"expand": True, "fill": 'both'}


class BlockFrame(BoilerFrame):
    """A block of Treeviews, and labels"""

    GENERAL_LABEL_TEXT = ''
    GENERAL_NOTEBOOK_TAB_001 = ''
    T1_GENERAL_NOTEBOOK_NUM_OF_COLS = 2
    GENERAL_NOTEBOOK_TAB_002 = ''
    LOWER_LABEL_TEXT = ''
    FONT = ('Helvetica bold', 20)

    def __init__(self, master, label_first: bool = True, mode: str = 'default'):  # noqa
        super().__init__(master)
        if mode == 'strict':
            pass
        self._upper = self.create_frame(self)
        self._lower = self.create_frame(self)
        self.notebook_general = self.create_notebook(self._upper)
        self.lower_notebook = self.create_notebook(self._lower)
        if label_first:
            self.__pack_label()
        self.N = (self.notebook_general, self.T1_GENERAL_NOTEBOOK_NUM_OF_COLS)
        self.notebook_general.pack(**widget_config.PACK_EXPAND_15x_5y)
        self.lower_notebook.pack(**widget_config.PACK_EXPAND_15x_5y)

        self._upper.pack(**PACK_EXPAND)
        self._lower.pack(**PACK_EXPAND)

        if mode == 'default':
            self.default_pack()
        else:
            pass

    def default_pack(self):

        self.__pack_tree_1_general_note()
        self.__pack_tree_2_general_note()
        self.__pack_lower()

    def __pack_label(self):
        # - Superior part
        self.general_label = self.create_label(self._upper, text=self.GENERAL_LABEL_TEXT, font=self.FONT)  # noqa
        self.general_label.pack()

    def __pack_tree_1_general_note(self):
        self.tree_1_notebook_general = self.create_tree(
            *self.N)
        self.tree_1_notebook_general.pack(**PACK_EXPAND_15x_5y)
        self.notebook_general.add(self.tree_1_notebook_general,
                                  text=self.GENERAL_NOTEBOOK_TAB_001)

    def __pack_tree_2_general_note(self):
        self.tree_2_notebook_general = self.create_tree(*self.N)  # noqa
        self.tree_2_notebook_general.pack(**PACK_EXPAND_15x_5y)
        self.notebook_general.add(self.tree_2_notebook_general,
                                  text=self.GENERAL_NOTEBOOK_TAB_002)

        # - Inferior part
    def __pack_lower(self):
        N1 = (self.lower_notebook, 2)
        self.tree_1_lower_notebook = self.create_tree(*N1)
        self.tree_2_lower_notebook = self.create_tree(*N1)
        self.tree_1_lower_notebook.pack(**widget_config.PACK_EXPAND_15x_5y)  # noqa
        self.tree_2_lower_notebook.pack(**widget_config.PACK_EXPAND_15x_5y)  # noqa
        self.lower_notebook.add(self.tree_1_lower_notebook, text='')  # noqa
        self.lower_notebook.add(self.tree_2_lower_notebook, text='')  # noqa


class BigBlockFrame(BoilerFrame):
    """ Base for other big blocks"""

    BIG_NOTEBOOK_TAB_001 = ''
    BIG_NOTEBOOK_TAB_1_COLS = 2
    BIG_NOTEBOOK_TAB_2_COLS = 1
    BIG_NOTEBOOK_TAB_002 = ''
    BIG_NOTEBOOK_TAB_003 = ''
    FONT = ('Helvetica bold', 20)

    def __init__(self, container):
        super().__init__(container)

    def pack_self(self):
        self.big_notebook = self.create_notebook(self)
        self.big_notebook.pack(side='right', expand=1, fill='both')

        self.tree_1_big_notebook = self.create_tree(
            self.big_notebook,
            self.BIG_NOTEBOOK_TAB_1_COLS,
            [self.BIG_NOTEBOOK_TAB_001, ]
        )
        self.tree_1_big_notebook.column('#1', width=300, minwidth=300)
        self.tree_1_big_notebook.pack(**widget_config.LEFT_PACK_EXP_PAD5_15)
        # - Creates a tree, a second tree
        self.tree_2_big_notebook = self.create_tree(
            self.big_notebook, self.BIG_NOTEBOOK_TAB_2_COLS, self.BIG_NOTEBOOK_TAB_002)  # noqa

        # self.tree_2_big_notebook.pack(**widget_config.RIGHT_PACK_EXP_PAD5_15)

        self.tree_3_big_notebook = self.create_tree(
            self.big_notebook, 1, [self.BIG_NOTEBOOK_TAB_003])
        # self.tree_3_big_notebook.pack(**widget_config.RIGHT_PACK_EXP_PAD5_15)

        self.big_notebook.add(self.tree_1_big_notebook)

        # self.big_notebook.add(self.tree_2_big_notebook)
        # self.big_notebook.add(self.tree_3_big_notebook)


class BigBlockPlain(BigBlockFrame):
    BIG_NOTEBOOK_TAB_1_COLS = 1

    def __init__(self, container):
        super().__init__(container)
        self.pack_self()


class BigBlockLabel(BigBlockFrame):
    """
    Construct a block element with a DoubleLabel to it.\n
    Use the class variables to configure the  number of cols and text.\n
    """
    BIG_NOTEBOOK_TAB_1_COLS = 2
    BIG_NOTEBOOK_TAB_2_COLS = 4

    TAG: DoubleLabel
    TAG_MENU = HorizontalButtons
    tag_menu: TAG_MENU

    def __init__(self, container, tag_menu=None):
        super().__init__(container)

        if tag_menu and hasattr(tag_menu, 'pack'):
            self.TAG_MENU = tag_menu

        self.tag_label = DoubleLabel(self)
        self.tag_label.pack()
        self.tag_menu = self.TAG_MENU(self)
        self.tag_menu.pack(fill='x', pady=8)
