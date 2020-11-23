from flask import Flask


def create_app():
    app = Flask(__name__)

    from bookmarks.views import bp_main
    app.register_blueprint(bp_main)

    return app
