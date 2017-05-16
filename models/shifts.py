from db import db
from datetime import datetime
from models.user import UserModel
import json
from flask import jsonify

class ShiftsModel(db.Model):
    __tablename__ = 'shifts'

    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(80), db.ForeignKey('user.username'))
    startTime = db.Column(db.String(10))
    endTime = db.Column(db.String(10))
    day = db.Column(db.String(10))
    user = db.relationship('UserModel', backref=db.backref('shifts'))

    def __init__(self, username, day, startTime, endTime):
        self.username = username
        self.day = day
        self.startTime = startTime
        self.endTime = endTime

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_username(cls, username):
        shifts = cls.query.filter_by(userName=username).all()
        shiftsInJson = {'shifts':[shift.serialize() for shift in shifts]}
        return shiftsInJson

    @classmethod
    def find_by_now(cls, today):
        shifts = cls.query.filter_by(day=today).all()
        shiftsInJson = {'shifts':[shift.serialize() for shift in shifts]}
        return shiftsInJson

    @classmethod
    def find_by_later(cls):
        shifts = cls.query.all()
        shiftsInJson = {'shifts':[shift.serialize() for shift in shifts]}
        return shiftsInJson

    @classmethod
    def remove_shift_after_trade(cls,username,startTime,endTime,day):
        cls.query.filter_by(userName=username,startTime=startTime,endTime=endTime,day=day).delete()
        db.session.commit()
    
    def serialize(self):
        return {
            'userName':self.userName,
            'startTime':self.startTime,
            'endTime':self.endTime,
            'day' : self.day
        }