from tkinter.ttk import Style


class MainStyleGenerator:

    MAIN: Style

    MENU_BTN ='menuButton.TButton'
    RED ='red'

    def __init__(self, master) -> None:
        self.STYLE = Style(master)
        self.STYLE.configure(
            'menuButton.TButton',
            font=('Helvetica bold', 10),
            justify="left",
            color='blue'
        )
        self.STYLE.configure('red', background='red')

    def helvetica_bold(self):
        return self.MENU_BTN

    def red(self):
        return self.RED
