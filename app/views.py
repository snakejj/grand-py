from flask import Flask, render_template, jsonify, request

from grandpy.grandpy import Grandpy

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        title="Grandpy",
        page_title="Grandpy, racontes nous une histoire !"
    )


@app.route("/answer", methods=["POST"])
def answer():
    question = request.form["question"]
    response = Grandpy(question)
    return jsonify(response.grandpy())
