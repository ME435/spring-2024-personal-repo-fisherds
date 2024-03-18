from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def mainpage():
    return render_template("index.html")

@app.route("/hello/<name>")
def hello_route(name):
    return f"Hello, {name}! Thanks for visiting!"
