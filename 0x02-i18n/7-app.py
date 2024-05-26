#!/usr/bin/env python3
"""
    7 - Flask App
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz
from datetime import datetime


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


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict:
    """Gets a user based on a user id."""
    user_id = request.args.get('login_as')
    if user_id is not None and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request() -> None:
    """routines before each request's resolution."""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Finds best match for supported languages."""
    locale = request.args.get('locale')

    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """Finds the best match for supported timezones."""
    try:
        timezone = request.args.get('timezone')
        if timezone:
            return pytz.timezone(timezone).zone
        if g.user and g.user.get('timezone'):
            return pytz.timezone(g.user.get('timezone')).zone
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index() -> str:
    """Default route."""
    current_time = format_datetime(datetime.now())
    return render_template("7-index.html", current_time=current_time)


if __name__ == "__main__":
    app.run()
