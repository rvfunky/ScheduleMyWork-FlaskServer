from flask_restful import Resource
from models.user import UserModel
from models.trade import TradeModel
from flask import request
from flask_jwt import JWT, jwt_required, current_identity

class Trade(Resource):
	@jwt_required()
	def post(self,purpose):
		data = request.get_json()

		print("data received")
		if(purpose=="offer"):
			print("offer received"+data['startTime'])
			trade = TradeModel(current_identity,None,data['startTime'],data['endTime'])
			trade.save_to_db()
		if(purpose=="accept"):
			print("accept received"+data['offeredUserName']);
			#offeredUser = UserModel.find_by_username(data['offeredUserName'])
			TradeModel.updateRecord(data['offeredUserName'],current_identity,data['startTime'],data['endTime'])	
		return {"data received": data}, 201

	def get(self):
		return{"message": "hello world"}, 200