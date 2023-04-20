from .view.apps import AbstractBoilerAPP
from .database import BaseDatabaseManager


class BoilerDatabaseHelper:
    """Abstract base to deal with view related tasks"""

    def __init__(self, database: BaseDatabaseManager) -> None:
        self.database = database
        pass


class BoilerViewHelper:
    def __init__(self, view: AbstractBoilerAPP) -> None:
        """Abstract base to deal with view related tasks"""
        self.view = view


class AbstractBoilerController(BoilerDatabaseHelper, BoilerViewHelper):
    """Abstract base to deal with view and database tasks"""

    def __init__(self,
                 view: AbstractBoilerAPP,
                 database: BaseDatabaseManager = None) -> None:
        self.view = view
        self.database = database


class BoilerMainController(BoilerDatabaseHelper, BoilerViewHelper):
    """Abstract base to deal with view and database tasks"""

    def __init__(self,
                 view: AbstractBoilerAPP,
                 database: BaseDatabaseManager = None) -> None:
        self.view = view
        self.database = database

    def run(self):
        self.view.setup(self)
        self.view.loop(self)
