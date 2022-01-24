
from tkinter import filedialog
from BoilerModel import Model, ModelDataBase
from BoilerView import App


class Controller:

    def __init__(self, model:Model, view:App, database: ModelDataBase):
        '''
        This function is for controller object
        merging both the model, with the data,
        and the view with the tkinter elemnts
        '''
        self.model = model
        self.view = view

    def run(self):
        '''
        This function is for the main TK object,
        setting up the widgets, and running the mainloop.
        '''
        self.view.setup(self)
        self.view.loop()

    ###############################
    ##                          ###
    ## BLOCK OF EXTRA FUNCTIONS ###
    ##                          ###
    ## ############################

    def OpenFile(self, view):
        """" Open File Function  """
        filename = filedialog.askopenfiles()
