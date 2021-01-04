from bookmarks import db

tags = db.Table('bookmark_tag',
                db.Column('bookmark_id', db.Integer, db.ForeignKey('bookmark.id')),
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                )  # middle table


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False, unique=True, index=True)

    @staticmethod
    def get_or_create(name):
        try:
            return Tag.query.filter_by(name=name).one()
        except Exception:
            return Tag(name=name)

    @staticmethod
    def all():
        return Tag.query.all()

    def __repr__(self):
        return f'<Tag {self.name}>'
