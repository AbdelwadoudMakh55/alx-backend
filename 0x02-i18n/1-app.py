#!/usr/bin/env python3
"""
Simple Flask app with jinja template
"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Class for configuration """
    LANGUAGES = ["en", "fr"]


app.config["BABEL_DEFAULT_LOCAL"] = "en"
app.config["BABEL_DEFAULT_TIMEZONE"] = "utc"
app.config["LANGUAGES"] = Config.LANGUAGES


@app.route("/")
def hello_holberton():
    """ Function that displays the Jinja template """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
