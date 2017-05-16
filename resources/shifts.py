from flask_restful import Resource
from models.user import UserModel
from models.shifts import ShiftsModel
from flask import request
from flask_jwt import JWT, jwt_required, current_identity
from datetime import date, timedelta

class Shifts(Resource):

	@jwt_required()
	def get(self,filter):
		if(filter == 'user'):
			return ShiftsModel.find_by_username(current_identity.username), 200
		if(filter == 'now'):
			print("todays date"+str(date.today().weekday()))
			day = date.today().weekday()
			if(day==0):
				print("Monday");
				return ShiftsModel.find_by_now("Monday"), 200
			if(day==1):
				print("Tuesday")
				return ShiftsModel.find_by_now("Tuesday"), 200
			if(day==2):
				print("Wednesday")
				return ShiftsModel.find_by_now("Wednesday"), 200
			if(day==3):
				print("Thursday")
				return ShiftsModel.find_by_now("Thursday"), 200
			if(day==4):
				print("Friday")
				return ShiftsModel.find_by_now("Friday"), 200
			if(day==5):
				print("Saturday")
				return ShiftsModel.find_by_now("Saturday"), 200
			if(day==6):
				print("Sunday")
				return ShiftsModel.find_by_now("Sunday"), 200

		if(filter == 'later'):
			 return ShiftsModel.find_by_later(), 200
			
			#return ShiftsModel.find_by_today("today"), 200