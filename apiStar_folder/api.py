from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def start():
    return render_template("index1.html")


# @app.route('/user/<username>')
# def show_user_profile(username):
# show the user profile for that user
#    return 'User %s' % username

# @app.route('/projects/')
# def projects():
#    return 'The project page'
