from flask_restful import Resource, Api

class Ledger(Resource):
	def __init__(self, db):
		self.db = db

	def get(self):
		statement = ("SELECT * FROM ledgers")
		self.db.run(statement)

