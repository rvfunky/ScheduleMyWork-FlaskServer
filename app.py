
from flask import Flask
from flask_restful import Api, Resource
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from resources.user import UserRegister
from resources.preference import Preference
from resources.trade import Trade
from resources.trades import Trades
from resources.schedule import Schedule
from resources.shifts import Shifts

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://raghu:schedulemywork@schedulemywork.cm8uunfgwrxe.us-west-2.rds.amazonaws.com:3306/schedulemywork'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'raghu'
api = Api(app)

@app.before_first_request
def create_tables():
	db.create_all()

jwt = JWT(app, authenticate, identity)  #/auth

class Test(Resource):
	@jwt_required()
	def post(self):
		return {"message":"hello world"}, 200

api.add_resource(Preference,'/preference')
api.add_resource(UserRegister,'/register')
api.add_resource(Test, '/test')
api.add_resource(Trade, '/trade/<string:purpose>')
api.add_resource(Trades,'/trades/<string:purpose>')
api.add_resource(Schedule,'/schedule')
api.add_resource(Shifts, '/shifts/<string:filter>')

if __name__ == '__main__':
	from db import db
	db.init_app(app)
	app.run(port = 5000,host='0.0.0.0',debug=True)
