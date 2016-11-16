from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String, Integer


class Lecturer(declarative_base()):
    __tablename__ = "lecturer"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    mail = Column(String)
    lectures = relationship('Lecture', back_populates="lecturers")
