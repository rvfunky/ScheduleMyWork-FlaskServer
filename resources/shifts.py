from flask_restful import Resource, reqparse
from models.user import UserModel
from flask import request
from flask_jwt import JWT, jwt_required, current_identity

class Shifts(Resource):

	@jwt_required()
	def get(self):
		return {"shifts":
			[{"day":"Monday",
			"slot":"A",
			"startTime":"8:00 AM",
			"endTime":"12:00 PM"},
			{"day":"Tuesday",
			"slot":"C",
			"startTime":"4:00 PM",
			"endTime":"8:00 PM"}]}, 200