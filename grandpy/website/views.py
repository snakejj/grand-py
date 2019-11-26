import flask

app = flask.Flask(__name__)


@app.route("/")
def home():
    return flask.render_template("home.html")


@app.route("/ajax")
def ajax():
    data = flask.request.get_json()
    response = grandpy(data.question)
    return flask.jsonify(response)
