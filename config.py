import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'some secret key'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI',
      default='postgresql://localhost/stackoverflow-lite')


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
  'development': DevelopmentConfig,
  'staging': StagingConfig,
  'production': ProductionConfig,
  'testing': TestingConfig
}
