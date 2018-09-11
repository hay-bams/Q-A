from .database import db
from .base.auditable_model import AuditableBaseModel
from .model_operations import ModelOperations


class Question(AuditableBaseModel, ModelOperations):
    title = db.Column(db.String(150))
    body = db.Column(db.Text)
    user_id = db.Column(db.String, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Question {}>'.format(self.title)
