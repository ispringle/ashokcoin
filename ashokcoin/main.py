from flask import Flask
from flask_restful import Api

from common.Sqlite import SQLITE

from resources.ashokcoin import Ashokcoin
from resources.ledger import Ledger
from resources.user import User
from resources.wallet import Wallet

app = Flask(__name__)
api = Api(app)

db = SQLITE()

def abort_if_user_doesnt_exist(user):
	check_users = (
			"SELECT username FROM users"
	)
	if user not in db.run(check_users):
		message = f"User {user} doesn't exist!"
		abort(404, message=message)


api.add_resource(Ashokcoin, '/ashokcoin/transact')
api.add_resource(Ledger, '/ashokcoin/ledger')
api.add_resource(User, '/ashokcoin/user/<user>')
api.add_resource(Wallet, '/ashokcoin/wallet/<user>')


if __name__  == "__main__":
	app.run(debug=True)

