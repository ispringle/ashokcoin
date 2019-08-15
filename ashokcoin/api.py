from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

LEDGER = {
        'ian': {'wallet': 1337},
        'ashok': {'wallet': 1000000},
}

def abort_if_user_doesnt_exist(user):
    if user not in LEDGER:
        message = f"User {user} doesn't exist!"
        abort(404, message=message)

class Ashokcoin(Resource):
    def get(self, user):
        abort_if_user_doesnt_exist(user)
        return LEDGER[user]


class Ledger(Resource):
    def get(self):
        return LEDGER


api.add_resource(Ledger, '/ashokcoin/ledger')
api.add_resource(Ashokcoin, '/ashokcoin/<user>')


if __name__  == "__main__":
    app.run(debug=True)

