from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker


class Repository:
    def __init__(self):
        engine = create_engine('postgresql://admin:admin@localhost:5432/sznk_db')
        self.Session = sessionmaker()
        self.Session.configure(bind=engine)
