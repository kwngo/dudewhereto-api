import flask_login
from sizzle.base import db
from logging import getLogger
from flask import session, abort
from flask_restful import Resource, reqparse
from sqlalchemy.exc import SQLAlchemyError
from hangtime.accounts.models import User
from flask_bcrypt import generate_password_hash

LOG = getLogger('hangtime')

parser = reqparse.RequestParser()
parser.add_argument('email', type=str)
parser.add_argument('password')
parser.add_argument('password_confirmation')

class Users(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', type=str)
        self.parser.add_argument('password')
        self.parser.add_argument('password_confirmation')
        super(User, self).__init__()


    def post(self):
        args = self.parser.parse_args()
        email = args['email']
        password = args['password']
        password = args['password_confirmation']
        email_exists = db.session.query(User).filter_by(email=email).count() > 0
        if email_exists:
            abort(400, message="User could not be created")

        if password != password_confirmation:
            abort(400, message="Passwords do not match.")

        pw_hash = generate_password_hash(password, 10)
        try:
            user = User(email, pw_hash.decode('utf-8'))
            db.session.add(user)
            db.session.commit()
            flask_login.login_user(user)
            return {'email': user.email}
        except SQLAlchemyError as e:
            LOG.error(f'User: User could not be created: {e}')

