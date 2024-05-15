#!/usr/bin/env python3
"""
Using the _ or gettext function to parametrize templates.
Using the message IDs home_title and home_header .
"""
from flask import Flask, render_template
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
      getting locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
      index
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
