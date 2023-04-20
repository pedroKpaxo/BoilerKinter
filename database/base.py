from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.base import Engine
from sqlalchemy import create_engine
from AGP.text_processor.utils.console import console
from .config import CONFIG

Base = CONFIG['BASE']


class BaseDatabaseManager:
    """
    Base class to initiate a connection to a database..

    """

    DEFAULT_DATABASE_NAME = 'database.db'

    def __init__(self):
        console.log('Database manager initiating ')
        self.base = Base
        self.engine = self.main_engine(self.DEFAULT_DATABASE_NAME)
        self.Session = self.create_session(self.engine)
        console.log('Database completed with sucess')

    def main_engine(self, path: str) -> Engine:
        """Creates a engine to the database"""

        p = f"sqlite:///{path}"
        engine = create_engine(str(p), echo=False, future=True)
        return engine

    def create_session(self, engine: Engine) -> sessionmaker:
        """Creates a session from the engine"""
        return sessionmaker(bind=engine)

    def create_all_tables(self) -> None:
        """Creates all the datables"""
        self.base.metadata.create_all(self.engine, checkfirst=True)
