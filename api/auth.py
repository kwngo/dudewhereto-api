import flask_login
from sizzle.base import db
from logging import getLogger
from flask import abort
from flask_restful import Resource, reqparse
from flask_bcrypt import check_password_hash

LOG = getLogger('sizzle')

parser = reqparse.RequestParser()
parser.add_argument('email', type=str)
parser.add_argument('password')

class Auth(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', type=str)
        self.parser.add_argument('password')
        super(Auth, self).__init__()

    def post(self):
        args = parser.parse_args()
        email = args['email']
        password = args['password']
        user = db.session.query(User).filter_by(email=email).one()
        if not user:
            abort(400, message="Something went wrong logging in")

        match = check_password_hash(user.password_hash, password)

        if not match:
            abort(400, message="Something went wrong logging in")

        flask_login.login_user(user)
        return {'login': user.get_id}

