from sznk.domain.lecture import Lecture
from sznk.repository import Repository


class LectureRepository(object):

    def create_lecture(self, lecture):
        session = Repository.Session()
        session.add(lecture)
        session.commit()

    def persist_lecture(self, lecture):
        session = Repository.Session()
        session.add(lecture)
        session.commit()


    def get_all_lectures(self):
        session = Repository.Session()
        return session.query(Lecture).all()

