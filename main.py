import os

from flask import Flask, Blueprint
from flask_restplus import Api

from api import api_blueprint
from api.models.database import db
from flask_migrate import Migrate

api = Api(api_blueprint, doc=False)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    
    app.register_blueprint(api_blueprint)

    db.init_app(app)
    
    from api.models import User

    migrate = Migrate(app, db)

    import api.views

    return app


