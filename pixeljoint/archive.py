import sqlite3

class Archive():
	"""
	This class represents the methods used on
	the management of the archive to keep track
	on downloaded icons.
	"""
	def __init__(self, path: str):
		self.conn = sqlite3.connect(path)
		self.cursor = self.conn.cursor()

		self.verify_table()

	@staticmethod
	def load(path: str):
		return Archive(path)

	def verify_table(self) -> None:
		"""
		Creates the table `downloaded` if it does not exists.
		"""
		self.cursor.execute('CREATE TABLE IF NOT EXISTS downloaded (id INTEGER)')
		self.conn.commit()

	def write(self, _id: int) -> None:
		"""
		Writes a icon id on the archive.

		Arguments:
			_id: The icon id.
		"""
		self.cursor.execute("INSERT INTO downloaded (id) VALUES (?)", (_id,))
		self.conn.commit()

	def exists(self, _id: int) -> bool:
		"""
		Verifies if the given icon id exists on the archive.

		Arguments:
			_id: The target icon id.
		Returns:
			bool: If the icon exists or not.
		"""
		self.cursor.execute("SELECT id FROM downloaded WHERE id=?", (_id,))
		result = self.cursor.fetchone()

		return result is not None

	def close(self) -> None:
		"""
		Closes the SQLITE3 Connection.
		"""
		self.conn.close()