class Archive():
	"""
	This class represents the methods used on
	the management of the archive to keep track
	on downloaded icons.
	"""
	def __init__(self, path: str):
		self.path: str = path

	@staticmethod
	def load(path: str):
		return Archive(path)

	def write(self, _id: int) -> None:
		"""
		Writes a icon id on the archive.

		Arguments:
			path: The archive file path.
			_id: The given icon id.
		"""
		with open(self.path, 'a', encoding="utf-8") as file:
			file.write(_id + '\n')

	def exists(self, _id: int) -> bool:
		"""
		Verifies if the given icon id exists on the archive.

		Arguments:
			path: The archive file path.
			_id: The target icon id.
		Returns:
			bool: If the icon exists or not.
		"""
		with open(self.path, 'r', encoding="utf-8") as file:
			return any(_id in line for line in file)