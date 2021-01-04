from flask import Blueprint, render_template

from bookmarks.bookmarks.models import Bookmark
from .tags.models import Tag

bp_main = Blueprint('main', __name__, url_prefix='/')


@bp_main.route('/')
def home():
    return render_template('index.html', new_bookmarks=Bookmark.latest(5))


@bp_main.context_processor
def inject_tags():
    return dict(all_tags=Tag.all())
