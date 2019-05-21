from sizzle.base import Base, db

class Post(Base):
    __tablename__ = 'posts'
    name = db.Column(db.String(), nullable=False, unique=True, index=True)
    url = db.Column(db.String, nullable=False)
    description = db.Column(db.String(), nullable=False)
    thumbnail = db.Column(db.String(), nullable=False)

    def __init__(self, name, url, description):
        self.name = name
        self.url = url
        self.description = description
        self.thumbnail = thumbnail

