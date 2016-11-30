import unittest

from sznk.domain import Lecturer
from sznk.repository.lecturer_repository import LecturerRepository


class LecturerRepositoryTest(unittest.TestCase):

    def test_get_all_lecturers(self):
        lecturer = Lecturer()
        lecturer_repository = LecturerRepository()
        lecturer.name = "Jerzy"
        lecturer.surname = "Dudek"
        lecturer.mail = "jerzy@dudek.pl"
        lecturer_repository.persist_lecturer(lecturer)
        lecturers = lecturer_repository.get_all_lecturers()
        self.assertEqual(len(lecturers), 1)
        self.assertEqual(lecturers[0].mail, "jerzy@dudek.pl")


if __name__ == '__main__':
    unittest.main()