from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String, Date


class Lecture(declarative_base()):
    __tablename__ = 'lecture'

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    date = Column(Date)
    place = Column(String)
    description = Column(String)
    max_people = Column(Integer)
    users = relationship("User", back_populate="lectures")
