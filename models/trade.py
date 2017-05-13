from db import db
from datetime import datetime
from models.user import UserModel
import json
from flask import jsonify

class TradeModel(db.Model):
    __tablename__ = 'trade'



    id = db.Column(db.Integer, primary_key=True)
    offeredUserName = db.Column(db.String(80), db.ForeignKey('user.username'))
    acceptedUserName = db.Column(db.String(80), db.ForeignKey('user.username'))
    startTime = db.Column(db.DateTime)
    endTime = db.Column(db.DateTime)
    offeredUser = db.relationship('UserModel', foreign_keys=[offeredUserName], backref=db.backref('offeredTrade'))
    acceptedUser = db.relationship('UserModel', foreign_keys=[acceptedUserName], backref=db.backref('acceptedTrade'))

    def __init__(self, offeredUser, acceptedUser, startTime, endTime):
        self.offeredUser = offeredUser
        self.acceptedUser = acceptedUser
        self.startTime = startTime
        self.endTime = endTime

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def updateRecord(cls, offeredUserName, acceptedUser, startTime, endTime):
        trade = cls.query.filter_by(offeredUserName=offeredUserName).first()
        print("printing trade"+trade.offeredUser.username)
        trade.acceptedUser = acceptedUser
        db.session.add(trade)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_username(cls, username, purpose):
        if(purpose=="offer"):
            trades = cls.query.filter_by(offeredUserName=username).all()
            tradesinjson = {'trades':[trade.serialize() for trade in trades]}
            return tradesinjson
        if(purpose=="accept"):
            trades = cls.query.filter_by(acceptedUserName=username).all()
            tradesinjson = {'trades':[trade.serialize() for trade in trades]}
            print(tradesinjson)
            return tradesinjson
    
    def serialize(self):
        return {
            'offeredUserName':self.offeredUserName,
            'acceptedUserName':self.acceptedUserName,
            'startTime':self.startTime.isoformat(),
            'endTime':self.endTime.isoformat()
        }