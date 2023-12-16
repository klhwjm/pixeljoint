import subprocess

class Misc():
	"""
	This class represents methods that are not linked
	on the other topics.
	"""
	@staticmethod
	def save(url: str, directory: str) -> None:
		"""
		Downloads a file on a directory using subprocess wget.

		Arguments:
			url: The target URL.
			directory: The target directory
		"""
		subprocess.run(["wget", "-nv", "-P", directory, url], check=True)