import sznk
from sznk.repository import Repository



class UserRepository(object):

    def persist_user(self, user):
        session = Repository.Session()
        session.add(user)
        session.commit()

    def get_all_users(self):
        session = Repository.Session()
        return session.query(sznk.domain.User).all()
