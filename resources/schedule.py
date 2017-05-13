from flask_restful import Resource
from flask_jwt import JWT, jwt_required, current_identity

class Schedule(Resource):

	@jwt_required()
	def post(self):
		return {"schedule":
			[{"day":"Monday",
			"slot":"A"},
			{"day":"Tuesday",
			"slot":"C"}]}, 200
	