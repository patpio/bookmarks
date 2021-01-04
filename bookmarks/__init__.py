import os

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
login_manager = LoginManager()

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'bookmarks.db')}"
    app.config['SECRET_KEY'] = 'dupa'

    from bookmarks.views import bp_main
    from .auth.views import bp_auth
    from .bookmarks.views import bp_bookmark
    from .tags.views import bp_tag

    app.register_blueprint(bp_main)
    app.register_blueprint(bp_auth)
    app.register_blueprint(bp_bookmark)
    app.register_blueprint(bp_tag)

    db.init_app(app)

    Migrate(app, db)

    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    return app

