from datetime import datetime

from sqlalchemy import desc

from bookmarks import db
from ..tags.models import tags, Tag


class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    _tags = db.relationship('Tag', secondary=tags, lazy='joined', backref=db.backref('bookmark', lazy='dynamic'))

    @staticmethod
    def latest(num):
        return Bookmark.query.order_by(desc(Bookmark.date)).limit(num)

    @property
    def tags(self):
        return ','.join([tag.name for tag in self._tags])

    @tags.setter
    def tags(self, text):
        if text:
            self._tags = [Tag.get_or_create(name) for name in text.split(',')]

    def __repr__(self):
        return f'<Bookmark {self.url}>'
