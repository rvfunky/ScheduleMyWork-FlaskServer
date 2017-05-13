from flask_restful import Resource
from models.user import UserModel
from models.trade import TradeModel
from flask import request
from flask_jwt import JWT, jwt_required, current_identity

class Trades(Resource):
	@jwt_required()
	def get(self,purpose):
		return TradeModel.find_by_username(current_identity.username,purpose), 200
