import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLE = True
    THREADS_PER_PAGE = 2
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SENTRY_CONFIG_DSN = ''
    JWT_COOKIE_SECURE = False
    JWT_COOKIE_CSRF_PROTECT = True

class ProdConfig(Config):
    NAME = 'production'
    DEBUG = False
    SENTRY_CONFIG_DSN = os.environ['SENTRY_CONFIG_DSN']
    JWT_COOKIE_SECURE = True

class StagingConfig(Config):
    NAME = 'staging'
    DEVELOPMENT = True
    DEBUG = True

class DevConfig(Config):
    NAME = 'development'
    DEVELOPMENT = True
    DEBUG = True

class TestConfig(Config):
    NAME = 'test'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ['TEST_DATABASE_URL']

app_config = {
        'development': DevConfig,
        'staging': StagingConfig,
        'production': ProdConfig,
        'testing': TestConfig
        }
