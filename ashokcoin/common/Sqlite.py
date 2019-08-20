import sqlite3

class SQLITE:
	def __init__(self):
		self.conn = sqlite3.connect('ashokcoin.db')
		self.cur = self.conn.cursor()

	def init(self):
		""" 
		Create tables for new database. Sqlite3 won't
		overwrite a table if it exists and CREATE is
		called, so this is safe to run even if the
		database has been setup properly already.
		"""
		users_statement = (
				"CREATE TABLE IF NOT EXIST users "
				"(user_id NOT NULL INTEGER PRIMARY KEY, "
				"username text NOT NULL)")
		wallets_statement = (
				"CREATE TABLE IF NOT EXIST wallets "
				"(wallet_id NOT NULL PRIMARY KEY, "
				"total INTEGER, user_id, "
				"FOREIGN KEY(user_id) REFERENCES users(user_id)")
		ledgers_statement = (
				"CREATE TABLE IF NOT EXIST ledgers "
				"(ledger_id NOT NULL PRIMARY KEY, "
				"date INTEGER, payer, payee, amount REAL"
				"FOREIGN KEY(payer) REFERENCES users(user_id), "
				"FOREIGN KEY(payee) REFERENCES users(user_id))")
		self.cur.execute(users_statement)
		self.cur.execute(wallets_statement)
		self.cur.execute(ledgers_statement)
		self.conn.commit()

		def run(self, statement):
			self.cur.execute(statement)
			return self.cur.fetchall()

		def update(self, statement):
			self.cur.execute(statement)
			self.conn.commit()


