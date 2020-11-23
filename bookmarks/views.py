from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

from bookmarks import db
from bookmarks.models import Bookmark
from bookmarks.forms import BookmarkForm

bp_main = Blueprint('main', __name__, url_prefix='/')


@bp_main.route('/')
def home():
    return render_template('index.html', new_bookmarks=Bookmark.latest(5))


@bp_main.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        bm = Bookmark(url=url, description=description)
        db.session.add(bm)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('add_form.html', form=form)
