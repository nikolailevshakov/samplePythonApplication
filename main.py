from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index(name="User"):
    name = "Kolya"
    return render_template("index.html", name=name)
@app.route("/cat")
def cat():
    return render_template("cat.html")