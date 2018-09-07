from .database import db
from .base.auditable_model import AuditableBaseModel
from .model_operations import ModelOperations


class User(AuditableBaseModel, ModelOperations):
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password = db.Column(db.String(50))

    def __repr__(self):
        return '<User {}>'.format(self.first_name)
