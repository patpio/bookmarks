from flask import Blueprint, render_template, url_for, abort, flash, request
from flask_login import login_required, current_user
from werkzeug.utils import redirect

from bookmarks import db
from .models import Bookmark
from ..bookmarks.forms import BookmarkForm

bp_bookmark = Blueprint('bookmark', __name__, url_prefix='/bookmarks')


@bp_bookmark.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data

        tags = form.tags.data

        bm = Bookmark(url=url, description=description, user=current_user, tags=tags)
        db.session.add(bm)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('bookmark_form.html', form=form, title='Add bookmark')


@bp_bookmark.route('/edit/<int:bookmark_id>', methods=['GET', 'POST'])
@login_required
def edit(bookmark_id):
    bookmark = Bookmark.query.get_or_404(bookmark_id)

    if current_user != bookmark.user:
        abort(403)

    form = BookmarkForm(obj=bookmark)

    if form.validate_on_submit():
        form.populate_obj(bookmark)  # add data from form to bookmark
        db.session.commit()

        flash(f'Saved {bookmark.description}')

        return redirect(url_for('auth.user', username=current_user.username))

    return render_template('bookmark_form.html', form=form, title='Edit bookmark')


@bp_bookmark.route('/delete/<int:bookmark_id>', methods=['GET', 'POST'])
@login_required
def delete(bookmark_id):
    bookmark = Bookmark.query.get_or_404(bookmark_id)

    if current_user != bookmark.user:
        abort(403)

    if request.method == 'POST':
        db.session.delete(bookmark)
        db.session.commit()

        flash(f'Bookmark {bookmark.description} has been removed.')

        return redirect(url_for('auth.user', username=current_user.username))

    else:
        flash('Please confirm deleting the bookmark.')

    return render_template('confirm_delete.html', bookmark=bookmark)
