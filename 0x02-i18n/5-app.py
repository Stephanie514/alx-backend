#!/usr/bin/env python3
"""
Flask Application with User Login Emulation
"""

from flask import Flask, render_template, g
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

# The mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """
    This returns user dictionary based on user ID or None if not found.
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """
    This sets the logged-in user as a global variable on flask.g.user.
    """
    user_id = int(request.args.get('login_as', 0))
    b.user = get_user(user_id)


@app.route('/')
def index():
    """
    Renders the index page with the appropriate welcome message.
    """
    if b.user:
        welcome_message = _("You are logged in as %(username)s.") % {'username': b.user['name']}
    else:
        welcome_message = _("You are not logged in.")
    return render_template('5-index.html', welcome_message=welcome_message)


if __name__ == '__main__':
    app.run(debug=True)
