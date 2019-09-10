import sqlite3

class SQLITE:
	def __init__(self):
		self.conn = sqlite3.connect('ashokcoin.db')
		self.cur = self.conn.cursor()
		self.create_if_not_exist()
		self.insert_test_data()

	def create_if_not_exist(self):
		""" 
		Create tables for new database. Sqlite3 won't
		overwrite a table if it exists and CREATE is
		called, so this is safe to run even if the
		database has been setup properly already.
		"""
		users_statement = (
				"CREATE TABLE IF NOT EXISTS users "
				"(user_id INTEGER PRIMARY KEY, "
				"username text NOT NULL)")
		wallets_statement = (
				"CREATE TABLE IF NOT EXISTS wallets "
				"(wallet_id NOT NULL PRIMARY KEY, "
				"total REAL, user_id, "
				"FOREIGN KEY(user_id) REFERENCES users(user_id))")
		ledgers_statement = (
				"CREATE TABLE IF NOT EXISTS ledgers "
				"(ledger_id NOT NULL PRIMARY KEY, "
				"date INTEGER, payer INTEGER, "
				"payee INTEGER, amount REAL, "
				"FOREIGN KEY(payer) REFERENCES users(user_id), "
				"FOREIGN KEY(payee) REFERENCES users(user_id))")
		self.cur.execute(users_statement)
		self.cur.execute(wallets_statement)
		self.cur.execute(ledgers_statement)
		self.conn.commit()

	def insert_test_data(self):
		users = ['ian', 'ashok', 'trump']
		wallets = [
				['ian', 1337],
				['ashok', 3],
				['trump', 1000000000]]
		for user in users:
			statement = (
					"INSERT INTO users "
					f"VALUES ('{user}')"
			)
			print(statement)
			self.update(statement)
		for wallet in wallets:
			statement = (
					"INSERT INTO wallets "
					f"VALUES ({wallet[1]}, "
					"(SELECT user_id FROM users "
					f"WHERE username = {wallet[0]}")
			print(statement)
			self.update(statement)

	def run(self, statement):
		self.cur.execute(statement)
		return self.cur.fetchall()

	def update(self, statement):
		self.cur.execute(statement)
		self.conn.commit()


