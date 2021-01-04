from flask import Blueprint, render_template

from ..tags.models import Tag

bp_tag = Blueprint('tag', __name__, url_prefix='/tags')


@bp_tag.route('/<name>')
def tag(name):
    tag = Tag.query.filter_by(name=name).first_or_404()
    return render_template('tag.html', tag=tag)
