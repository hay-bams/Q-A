from .database import db


class ModelOperations():
    def save(self):
        db.session.add(self)
        db.session.commit()

    def get(cls, id):
        return cls.query.filter_by(id=id).first()

    def update_(self, **kwargs):
        for field, value in kwargs.item():
            setattr(self, field, value)
        db.session.commit()

    def query_(cls):
        return cls.query.all()

    def delete(cls, id):
        db.session.delete(id)

    def count(cls):
        return cls.query.count()