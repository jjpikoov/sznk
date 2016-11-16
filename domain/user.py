from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String, Integer


class User(declarative_base()):
    __tablename__ = 'user_'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    mail = Column(String)
    lectures = relationship('Lecture', back_populates="user")



