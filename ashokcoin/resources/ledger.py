from flask_restful import Resource, Api

class Ledger(Resource):
	def get(self):
		return LEDGER

