#!/usr/bin/env python3
"""
Basic Flask app with Babel for i18n
"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
    Configuration class for the Flask app.

    Attributes:
        LANGUAGES (list): List of supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale (language) for the app.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """
        index
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
