from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url, Regexp


class BookmarkForm(FlaskForm):
    url = URLField('URL for bookmark:', validators=[DataRequired(), url()])
    description = StringField('Optional description')
    tags = StringField('Tags', validators=[Regexp(r'[a-zA-Z0-9, ]*$', message='Tags can only contain letters and numbers')])
    # $ can not end for any other letter/number
    submit = SubmitField('Submit')
