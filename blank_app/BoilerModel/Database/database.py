from .config import Session, Base, Engine
from .Models.model import TODO


class ModelDataBase:
    '''
    This is the main database instance.
    It imports the configurations and creates a engine for connection when the 
    app is initialized.
    '''

    def __init__(self) -> None:
        self.Engine = Engine
        self.BASE = Base
        self.BASE.metadata.create_all(self.Engine)
        self.session = Session()

    def create(self, data: dict, *args, **kargs):
        '''
        Creates a instance of the todo object.
        '''

        t = TODO(task=data['TASK'])
        print(type(t))
        y = isinstance(t, TODO)
        print(y)
        self.session.add(t)
        self.session.commit()

    def queryName(self, task: str, *args):
        q = self.session.query(TODO).filter(TODO.task == task).first()
        print('_________________')
        y = isinstance(q, TODO)
        print(y)
        print('_________________')
        print(q)
        print(type(q))
        self.session.delete(q)
        self.session.commit()

    @property
    def query(self) -> list[TODO]:
        query = self.session.query(TODO)
        return query.all()
