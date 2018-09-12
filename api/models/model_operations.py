from .database import db


class ModelOperations():
    """Mixin class with generic model operations."""
    def save(self):
        """
        Save a model instance
        """
        db.session.add(self)
        db.session.commit()
        return self

    def _update(self, **kwargs):
        """
        update entries
        """
        for field, value in kwargs.items():
            setattr(self, field, value)
        db.session.commit()

    @classmethod
    def get(cls, id):
        """
        return entries by id
        """
        return cls.query.filter_by(id=id).first()

    @classmethod
    def query_(cls):
        return cls.query

    @classmethod
    def delete(cls, model):
        db.session.delete(model)
        db.session.commit()

    @classmethod
    def count(cls):
        return cls.query.count()