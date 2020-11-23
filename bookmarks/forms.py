from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url


class BookmarkForm(FlaskForm):
    url = URLField('URL for bookmark:', validators=[DataRequired(), url()])
    description = StringField('Optional description')