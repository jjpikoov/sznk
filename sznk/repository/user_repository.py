from sznk.repository.repository import Repository


class UserRepository(object):

    def persist_user(self, user):
        session = Repository.Session()
        session.add(user)

    def get_all_users(self):
        return []
