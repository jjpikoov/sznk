from __future__ import absolute_import
import unittest

from sznk.domain import Lecture
from sznk.repository import LectureRepository


class LectureRepositoryTest(unittest.TestCase):

    def test_get_all_lectures(self):
        lecture = Lecture()
        lecture_repository = LectureRepository()
        lecture.title = "Wyklad1"
        lecture.place = "Sala1"

        lecture_repository.persist_lecture(lecture)

        lectures = lecture_repository.get_all_lectures()
        self.assertEqual(len(lectures), 1)
        self.assertEqual(lectures[0].title, "Wyklad1")


if __name__ == '__main__':
    unittest.main()