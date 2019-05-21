from sizzle.base import Base, db

class Shop(Base):
    __tablename__ = 'shops'
    name = db.Column(db.String(), nullable=False, unique=True, index=True)
    url = db.Column(db.String, nullable=False)
    description = db.Column(db.String(), nullable=False)
    thumbnail = db.Column(db.String(), nullable=False)

    def __init__(self, name, url, description):
        self.name = name
        self.url = url
        self.description = description
        self.thumbnail = thumbnail

