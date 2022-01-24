
from BoilerView import App
from BoilerModel import Model, ModelDataBase
from BoilerControl import Controller


if __name__ == "__main__":
    MainApp = Controller(Model, App(), ModelDataBase())
    MainApp.run()
