from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker


class Repository:
    Session = sessionmaker()
    engine = create_engine('postgresql://admin:admin@localhost:5432/sznk_db')
    Session.configure(bind=engine)
