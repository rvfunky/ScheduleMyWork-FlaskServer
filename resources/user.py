from flask_restful import Resource, reqparse
from models.user import UserModel
from flask import request

class UserRegister(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('username',
		type=str,
		location='form',
		required=True,
		help="This field cannot be left blank")
	parser.add_argument('password',
		type=str,
		location='form',
		required=True,
		help="this field cannot be left blank")

	def post(self):
		data = request.get_json()

		if UserModel.find_by_username(data['username']):
			return {"message":"a user with the given username already exists"}, 400

		user = UserModel(data['username'],data['password'])
		user.save_to_db()

		return {"message": "user created successfully"}, 201

	def get(self):
		return{"message": "hello world"}, 200