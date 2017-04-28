from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String, Integer

from sznk.domain.model_base import ModelBase


class Lecturer(ModelBase.Base):
    __tablename__ = "lecturer"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    mail = Column(String)
    lectures = relationship('Lecture', back_populates="lecturer")
