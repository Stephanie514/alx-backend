#!/usr/bin/env python3
"""
Flask Application for Internationalization (i18n)
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)

AVAILABLE_LOCALES = ["en", "fr"]


@babel.localeselector
def get_locale():
    """
    Select the locale for the request.
    If the 'locale' parameter is present and valid, use it.
    Otherwise, fall back to the default behavior.
    """
    requested_locale = request.args.get('locale')
    if requested_locale and requested_locale in AVAILABLE_LOCALES:
        return requested_locale
    return request.accept_languages.best_match(AVAILABLE_LOCALES)


@app.route('/')
def index():
    """
    Render the index page with translated titles and headers.
    """
    return render_template('4-index.html',
                           title=_('home_title'), header=_('home_header'))


if __name__ == '__main__':
    app.run(debug=True)
