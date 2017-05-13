from flask_restful import Resource
from models.preference import PreferenceModel
from models.user import UserModel
from flask import request
from flask_jwt import JWT, jwt_required, current_identity

class Preference(Resource):
	@jwt_required()
	def post(self):
		data = request.get_json()

		print("data received")
		preference = PreferenceModel(current_identity,data['startTime'],data['endTime'])
		preference.save_to_db()
		return {"data received": data}, 201

	def get(self):
		return{"message": "hello world"}, 200