from repository import Repository


class UserRepository:

    def persist_user(self, user):
        session = Repository.Session()
        session.add(user)
