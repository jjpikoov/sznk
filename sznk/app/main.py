from flask import Flask
from flask import send_from_directory
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
def show_main_page():
    return render_template('main.j2')

@app.route('/resources/<path:path>')
def access_static_resources(path):
    return send_from_directory('resources', path)

if __name__ == "__main__":
    app.run(debug=True)