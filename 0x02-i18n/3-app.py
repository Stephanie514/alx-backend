#!/usr/bin/env python3
"""
    Flask App
"""

from flask import Flask
from flask_babel import Babel
from flask import render_template
from flask import request


class Config:
    """
        Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
        the get_locale function
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
        Index
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
