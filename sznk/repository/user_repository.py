from sznk.repository.repository import Repository
from sznk.domain import User


class UserRepository(object):

    def persist_user(self, user):
        session = Repository.Session()
        session.add(user)
        session.commit()

    def get_all_users(self):
        session = Repository.Session()
        return session.query(User).all()
