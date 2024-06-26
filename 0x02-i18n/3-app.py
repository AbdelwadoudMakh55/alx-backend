#!/usr/bin/env python3
"""
Simple Flask app with jinja template and flask_babel for i18n
"""


from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Class for configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Get accepted languages from the browser requests header """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def hello_holberton():
    """ Function that displays the Jinja template """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
