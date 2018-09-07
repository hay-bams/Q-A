import os

from flask import Flask, Blueprint, jsonify
from flask_restplus import Api
from api import api_blueprint
from flask_migrate import Migrate

from api.models.database import db
from api.middleware.base_validator import ValidationError, middleware_blueprint



api = Api(api_blueprint, doc=False)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(middleware_blueprint)
    app.register_blueprint(api_blueprint)

    db.init_app(app)

    from api.models import User

    migrate = Migrate(app, db)

    import api.views

    return app


@api.errorhandler(ValidationError)
@middleware_blueprint.app_errorhandler(ValidationError)
def handle_exception(error):
    """Error handler called when a ValidationError Exception is raised"""

    response = jsonify(error.to_dict())
    response.status_code = error.status_code  # not needed
    return response
