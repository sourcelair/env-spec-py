from flask import Flask, request
from flask import render_template
import env_spec


app = Flask(__name__)


@app.route("/")
def input_envspec():
    return render_template("index.html")


@app.route("/api/render/", methods=["POST"])
def render_envspec():
    data = request.form
    html_output = env_spec.render_env_spec_to_html(data)
    return html_output
    # return render_template("index.html")
