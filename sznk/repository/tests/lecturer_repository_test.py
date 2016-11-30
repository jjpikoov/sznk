import unittest

from sznk.domain import Lecturer
from sznk.repository.lecturer_repository import LecturerRepository


class LecturerRepositoryTest(unittest.TestCase):

    def test_persisting_lecturers(self):
        lecturer = Lecturer()
        lecturer_repository = LecturerRepository()
        lecturer.name = "Wyklad"
        lecturer_repository.persist_lecturer(lecturer)


if __name__ == '__main__':
    unittest.main()