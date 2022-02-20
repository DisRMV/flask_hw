from flask_sqlalchemy import SQLAlchemy
from app import db


class Advertisements(db.Model):

    __tablename__ = 'advertisements'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(120), nullable=True)
    inception_date = db.Column(db.Date, default=db.func.now())
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'inception_date': self.inception_date,
            'owner_id': self.owner_id
        }


class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(128))
    advertisements = db.relationship('Advertisements', backref='owner')







