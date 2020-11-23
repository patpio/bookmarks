from bookmarks import db


class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, nullable=False)