from flask_restful import Resource, Api

class User(Resource):
	def get(self, user):
		abort_if_user_doesnt_exist(user)
		get_user = (
				"SELECT * FROM users "
				f"WHERE username = {user}"
		)
		result = db.run(get_user)
		return result

