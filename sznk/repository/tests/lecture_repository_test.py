import unittest

from sznk.domain import Lecture
from sznk.repository.lecture_repository import LectureRepository


class LectureRepositoryTest(unittest.TestCase):

    def test_persisting_lectures(self):
        lecture = Lecture()
        lecture_repository = LectureRepository()
        lecture.name = "Wyklad"
        lecture_repository.persist_lecture(lecture)


if __name__ == '__main__':
    unittest.main()