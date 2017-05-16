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
    startTime = db.Column(db.String(10))
    endTime = db.Column(db.String(10))
    day = db.Column(db.String(10))
    offeredUser = db.relationship('UserModel', foreign_keys=[offeredUserName], backref=db.backref('offeredTrade'))
    acceptedUser = db.relationship('UserModel', foreign_keys=[acceptedUserName], backref=db.backref('acceptedTrade'))

    def __init__(self, offeredUser, acceptedUser, startTime, endTime, day):
        self.offeredUser = offeredUser
        self.acceptedUser = acceptedUser
        self.startTime = startTime
        self.endTime = endTime
        self.day = day

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def updateRecord(cls, offeredUserName, acceptedUser, startTime, endTime, day):
        trade = cls.query.filter_by(offeredUserName=offeredUserName,startTime=startTime,endTime=endTime,day=day).first()
        #print("printing trade"+trade.offeredUser.username)
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
        if(purpose=="open"):
            trades = cls.query.filter_by(acceptedUserName=None).all()
            tradesinjson = {'trades':[trade.serialize() for trade in trades]}
            print(tradesinjson)
            return tradesinjson


        
    
    def serialize(self):
        return {
            'offeredUserName':self.offeredUserName,
            'acceptedUserName':self.acceptedUserName,
            'startTime':self.startTime,
            'endTime':self.endTime,
            'day' : self.day
        }