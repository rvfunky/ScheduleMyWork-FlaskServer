from db import db
from datetime import datetime
from models.user import UserModel

class PreferenceModel(db.Model):
    __tablename__ = 'preference'



    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), db.ForeignKey('user.username'))
    startTime = db.Column(db.DateTime)
    endTime = db.Column(db.DateTime)
    user = db.relationship('UserModel', backref=db.backref('preference'))
    
    def __init__(self, user, startTime, endTime):
        self.user = user
        self.startTime = startTime
        self.endTime = endTime

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()