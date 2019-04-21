from dudewhereto.base import Base, db


class User(Base):
    __tablename__ = 'users'
    email = db.Column(db.String(), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(), nullable=False)
    confirmation_token = db.Column(db.String)
    confirmed_at = db.Column(db.DateTime)
    confirmation_sent_at = db.Column(db.DateTime)

    def __init__(self, email, password_hash, account_id, roles=None, confirmation_token=None, confirmed_at=None, confirmation_sent_at=None):
        self.email = email
        self.password_hash = password_hash
        self.account_id = account_id
        self.confirmation_token = confirmation_token
        self.confirmed_at = confirmed_at
        self.confirmation_sent_at = confirmation_sent_at

