#!/usr/bin/env python3
"""
Using the _ or gettext function to parametrize templates.
Using the message IDs home_title and home_header .
"""
from flask import Flask, render_template
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index():
    return render_template('3-index.html',
                           title=_('home_title'), header=_('home_header'))


@app.route('/')
def index():
    """
      index
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
