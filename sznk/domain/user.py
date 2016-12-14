from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String, Integer

from sznk.domain.model_base import ModelBase
from sznk.repository import Repository


class User(ModelBase.Base):
    __tablename__ = 'user_'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    mail = Column(String)
    lectures = relationship('Lecture', back_populates="user")

if __name__ == "__main__":
    User.metadata.create_all(Repository.engine)
