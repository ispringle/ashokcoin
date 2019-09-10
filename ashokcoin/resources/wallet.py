from flask_restful import Resource, Api
from flask import Flask

class Wallet(Resource):
	def __init__(self, db):
		self.db = db

	def get(self, user):
		# abort_if_user_doesnt_exist(user)
		get_user = (
				"SELECT * FROM wallets "
				"WHERE user_id = "
				"(SELECT user_id from users "
				f"WHERE username = '{user}')"
		)
		result = self.db.run(get_user)
		return result

	def abort_if_user_doesnt_exist(self, user):
		check_users = (
				"SELECT username FROM users"
		)
		if user not in self.db.run(check_users):
			message = f"User {user} doesn't exist!"
			flask.abort(404, message=message)

