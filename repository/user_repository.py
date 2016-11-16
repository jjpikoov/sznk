from repository import Repository


class UserRepository(Repository):

    def persist_user(self, user):
        session = self.Session()
        session.add(user)
        session.commit()