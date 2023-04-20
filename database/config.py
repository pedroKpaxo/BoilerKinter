from typing import NewType
from sqlalchemy.orm import declarative_base

CONFIG = {
    "BASE":declarative_base()
}
DeclarativeBase = NewType('DeclarativeBase', CONFIG['BASE'])
