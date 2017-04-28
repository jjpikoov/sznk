import unittest

from sznk.domain import User
from sznk.repository.user_repository import UserRepository


class UserRepositoryTest(unittest.TestCase):

    def test_persisting_users(self):
        user = User()
        user_repository = UserRepository()
        user.name = "pawel"
        user_repository.persist_user(user)

    def test_get_all_users(self):
        user = User()
        user_repository = UserRepository()
        user.name = "Adam"
        user.surname = "Malysz"
        user.mail = "adam@malysz.pl"
        user_repository.persist_user(user)
        users = user_repository.get_all_users()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].mail, "adam@malysz.pl")


if __name__ == '__main__':
    unittest.main()