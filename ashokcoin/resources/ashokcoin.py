from flask_restful import Resource, Api
from flask import Flask

class Ashokcoin(Resource):
	def __init__(self, db):
		self.db = db

	def get(self, sender, recipient, amount):
		# abort_if_user_doesnt_exist(user)
		statement = (
				"INSERT INTO ledgers "
				"(payer, payee, amount) VALUES ("
				"(SELECT user_id FROM users "
				f"WHERE username = '{sender}'), "
				"(SELECT user_id FROM users "
				f"WHERE username = '{recipient}'), "
				f"{amount})"
		)
		result = self.db.run(statement)
		return result

	def abort_if_user_doesnt_exist(self, user):
		check_users = (
				"SELECT username FROM users"
		)
		if user not in self.db.run(check_users):
			message = f"User {user} doesn't exist!"
			flask.abort(404, message=message)

