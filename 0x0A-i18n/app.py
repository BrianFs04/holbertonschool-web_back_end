#!/usr/bin/env python3
"""
Infer appropriate time zone
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/")
def root_path():
    """Root route"""
    return render_template("6-index.html")


@babel.localeselector
def get_locale():
    """Get locale language from request"""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user():
    """Returns a user dictionary or None if the ID cannot be
    found or if login_as was not passed"""
    try:
        return users[int(request.args.get("login_as"))]
    except Exception:
        return None


@app.before_request
def before_request():
    """Uses get_user to find a user if any"""
    g.user = get_user()


@babel.timezoneselector
def get_timezone():
    """Gets the timezone"""
    try:
        if request.args.get("timezone"):
            timezone = request.args.get("timezone")
            pytz.timezone(timezone)
        elif g.user and g.user.get("timezone"):
            timezone = g.user.get("timezone")
            pytz.timezone(timezone)
        else:
            timezone = app.config["BABEL_DEFAULT_TIMEZONE"]
            pytz.timezone(timezone)
    except pytz.exceptions.UnknownTimeZoneError:
        timezone = "UTC"

    return timezone


if __name__ == "__main__":
    app.run()
