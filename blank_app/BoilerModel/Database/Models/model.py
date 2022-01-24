from sqlalchemy import Column, Integer, String,DATETIME
import datetime
from ..config import Base
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship


class TODO(Base):
    '''
    Instance of a To-Do.
    '''
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    
    task = Column(String)
    date = Column(DATETIME)

    def __init__(self,task):
        super(Base,self).__init__()
        
        self.task=task
        self.date = datetime.datetime.now()
    def __repr__(self):
        return "<Todo(task='%s', date='%s', )>" % (self.task, self.date)