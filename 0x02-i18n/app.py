#!/usr/bin/env python3
"""
Flask Application with Babel for i18n and timezone handling
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime, _
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
    """
    Retrieve a user based on the 'login_as' query parameter.

    Returns:
        dict: User dictionary if found, else None.
    """
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request() -> None:
    """
    Load user before each request if 'login_as' query
    parameter is present.
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for supported languages.

    Returns:
        str: Locale string.
    """
    locale_param = request.args.get('locale')
    if locale_param in app.config['LANGUAGES']:
        return locale_param
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Determine the best match for supported timezones.

    Returns:
        str: Timezone string.
    """
    try:
        timezone_param = request.args.get('timezone')
        if timezone_param:
            return pytz.timezone(timezone_param).zone
        if g.user and g.user.get('timezone'):
            return pytz.timezone(g.user.get('timezone')).zone
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index() -> str:
    """
    The home route.

    Returns:
        str: Rendered HTML template.
    """
    current_time = format_datetime(datetime.now(pytz.timezone(get_timezone())))
    return render_template("5-index.html", current_time=current_time)


if __name__ == "__main__":
    app.run(debug=True)
