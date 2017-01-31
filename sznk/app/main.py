from flask import Flask
from flask import redirect, request, send_from_directory, url_for
from flask.templating import render_template
from sznk.domain.model_base import ModelBase
from sznk.repository import LectureRepository
from sznk.domain import Lecture
from sznk.repository.repository import Repository

app = Flask(__name__)


@app.route("/")
def show_main_page():
    return render_template('main.j2')


@app.route("/add_lecture", methods=["GET", "POST"])
def add_lecture():
    if request.method == "GET":
        return render_template("create_lecture.j2")
    elif request.method == "POST":
        lecture = Lecture(
            title=request.form['title'],
            place=request.form["place"],
            description=request.form["description"],
        )
        LectureRepository().persist_lecture(lecture)
    return render_template("success.j2")


@app.route("/all_lectures")
def list_all_lectures():
        lectures = LectureRepository().get_all_lectures()
        return render_template("all_lectures.j2", lectures=lectures)


@app.route('/resources/<path:path>')
def access_static_resources(path):
    return send_from_directory('resources', path)


if __name__ == "__main__":
    ModelBase.Base.metadata.create_all(Repository.engine)
    app.run(debug=True)
