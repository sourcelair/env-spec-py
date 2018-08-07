from flask import Flask
from flask import request
from flask import render_template
import env_spec

app = Flask(__name__)


@app.route("/")
def input_envspec():
    return render_template("index.html")


@app.route("/api/render/", methods=["POST"])
def render_envspec():
    data = request.data
    data = data.decode("utf-8")

    html_output = env_spec.render_env_spec_to_html(data)

    return html_output
