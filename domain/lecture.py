from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Date

from domain.model_base import ModelBase


class Lecture(ModelBase.Base):
    __tablename__ = 'lecture'

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    date = Column(Date)
    place = Column(String)
    description = Column(String)
    max_people = Column(Integer)
    user_id = Column(Integer, ForeignKey('user_.id'))
    user = relationship("User", back_populates="lectures")
