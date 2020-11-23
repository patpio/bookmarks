from datetime import datetime

from sqlalchemy import desc

from bookmarks import db


class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(300))

    @staticmethod
    def latest(num):
        return Bookmark.query.order_by(desc(Bookmark.date)).limit(num)
