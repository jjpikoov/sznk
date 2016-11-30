import unittest

from sznk.domain import User
from sznk.repository.user_repository import UserRepository


class UserRepositoryTest(unittest.TestCase):

    def test_persisting_users(self):
        user = User()
        user_repository = UserRepository()
        user.name = "pawel"
        user_repository.persist_user(user)


if __name__ == '__main__':
    unittest.main()