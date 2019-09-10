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


api.add_resource(Ashokcoin, '/ashokcoin/transact/<sender>/<recipient>/<amount>', resource_class_args={db})
api.add_resource(Ledger, '/ashokcoin/ledger', resource_class_args={db})
api.add_resource(User, '/ashokcoin/user/<user>', resource_class_args={db})
api.add_resource(Wallet, '/ashokcoin/wallet/<user>', resource_class_args={db})


if __name__  == "__main__":
	app.run(debug=True)

