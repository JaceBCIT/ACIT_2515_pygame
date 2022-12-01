from flask import Flask, render_template, request
from models import GetScore

app = Flask(__name__)

@app.route("/")
def home():
    data = GetScore()
    name = data.users
    score = data.high_score
    length = len(name)

    return render_template("dashboard.html", name=name, score=score, length=length)

@app.route("/player")
def display_one_user():
    data = GetScore()
    json_dict = data.board
    uname = request.args.get('name')

    return render_template("oneplayer.html", json_dict=json_dict, uname=uname)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
