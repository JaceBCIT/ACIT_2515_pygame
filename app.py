import operator
from flask import Flask, render_template, request
from models import GetScore

app = Flask(__name__)

@app.route("/")
def home():
    data = GetScore()
    json_dict = data.board
    score_list = sorted(json_dict.items(), key=operator.itemgetter(1), reverse=True)
    

    return render_template("dashboard.html", score_list=score_list, json_dict=json_dict)

@app.route("/player")
def display_one_user():
    data = GetScore()
    json_dict = data.board
    uname = request.args.get('name')

    return render_template("oneplayer.html", json_dict=json_dict, uname=uname)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
