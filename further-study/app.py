from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def ask_story():
    """Show list-of-stories form"""
    return render_template("select-story.html", stories=stories.values())


