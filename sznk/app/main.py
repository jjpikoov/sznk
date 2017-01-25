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

@app.route("/add_lecture")
def add_lecture():
    return render_template("create_lecture.j2")

@app.route("/lecture", methods=["POST"])
def post_lecture():
    lecture = Lecture(
        title=request.form['title'],
        place=request.form["place"],
        description=request.form["description"],
    )
    LectureRepository().create_lecture(lecture)
    return redirect(url_for("show_main_page"))

@app.route('/resources/<path:path>')
def access_static_resources(path):
    return send_from_directory('resources', path)

if __name__ == "__main__":
    ModelBase.Base.metadata.create_all(Repository.engine)
    app.run(debug=True)