from flask import Blueprint, render_template

from bookmarks.models import Bookmark

bp_main = Blueprint('main', __name__, url_prefix='/')


@bp_main.route('/')
def home():
    return render_template('index.html', new_bookmarks=Bookmark.latest(5))
