#!/usr/bin/env python
"""
Simple Flask app with jinja template
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def hello_holberton():
    """ Function that displays the Jinja template """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
