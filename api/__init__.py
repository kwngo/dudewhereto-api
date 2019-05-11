import flask_login
import json
import os
from flask import Flask, request, jsonify, render_template
from flask_restful import Api
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from config import app_config
from dudewhereto.base import db

migrate = Migrate()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    migrate.init_app(app, db)

    login_manager=flask_login.LoginManager()
    login_manager.setup_app(app)

    @login_manager.user_loader
    def load_user(email):
        return User.query.get(email)

    CORS(app, supports_credentials=True)

    from .users import Users
    from .auth import Auth
    from .shops import Shops

    api = Api(app)
    api.add_resource(Users, '/users')
    api.add_resource(Auth, '/auth')
    api.add_resource(Shops, '/shops')


    @app.route("/")
    def hello():
       return "Hello world!"

    @app.route('/logout')
    @flask_login.login_required
    def logout():
        flask_login.logout_user()
        return 'Logged out!'

    return app


if __name__ == '__main__':
    print(os.environ['APP_SETTINGS'])
    app = create_app()
    app.config.from_object(app_config[os.environ['APP_SETTINGS']])
    app.run(debug=True)

