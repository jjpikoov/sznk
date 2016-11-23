from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
def show_main_page():
    return render_template('main.j2')

if __name__ == "__main__":
    app.run(debug=True)