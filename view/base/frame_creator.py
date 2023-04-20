from tkinter.ttk import Button, Frame, Label, Notebook, Scrollbar, Treeview


SCROLLBAR_PACK = {"side": 'right', "fill": 'y'}


class Creator:

    def create_label(self, master, text: str, font: tuple = None) -> Label:
        """Returns a ttk.Label"""
        return Label(master, text=text, font=font)

    def create_notebook(self, container):
        """Returns a ttk.Notebook"""
        return Notebook(container)

    def create_tree(self,
                    tree_master: Frame or Notebook,
                    col_nums: int,
                    col_text: list[str] = None) -> Treeview:
        """
        Function to build a custom treeview with scrollbar.
        @ params:
            tree_master = Frame or notebook, works as a master\n
            col_nums = Ineger representing the number of cols\n
            col_text = opcional names the columns\n
        """

        ids = [f'#{_}' for _ in range(1, col_nums+1)]
        tree = Treeview(tree_master, columns=ids, show="headings")
        if col_text:
            col_config = zip(ids, col_text)
            for c in col_config:
                tree.column(c[0])
                tree.heading(c[0], text=c[1])
        else:
            for id in ids:
                tree.column(id)
                tree.heading(id, text='')
        scrollbar = Scrollbar(tree)
        scrollbar.pack(**SCROLLBAR_PACK)
        scrollbar.config(command=tree.yview)
        tree.config(yscrollcommand=scrollbar.set)
        return tree

    def create_frame(self, master):
        """Returns a ttk.Frame"""
        return Frame(master=master)

    def create_button(self, master, text):
        """Returns a ttk.Button"""
        return Button(master=master, text=text)


class BoilerFrame(Frame, Creator):
    """
    A frame with super powers
    Capable of creating treeviews, notebooks, frames and buttons.
    """

    def __init__(self, container):
        super().__init__(container)
