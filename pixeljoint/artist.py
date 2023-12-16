from pixeljoint.httpclient import HttpClient
import re
import os

class Artist():
	def __init__(self, name: str, _id: int):
		self.name: str = name
		self.id: int = _id

	@staticmethod
	def parse(url: str):
		"""
		Parses artist information from its profile URL.

		Arguments:
			url: The artist profile URL.
		Returns:
			Artist: A parsed Artist object.
		"""
		name_pattern = r'<title>Pixel Artist - (.+)</title>'

		match = re.search(name_pattern, HttpClient.get(url))
		_id = url.split('/')[-1].split('.')[0]

		return Artist(match[1], _id)

	def icons(self, page: int) -> list:
		"""
		Parses the artist icons from a given page.

		Arguments:
			page: The target page.
		Returns:
			list: A list of the page icons.
		"""
		icons_pattern = r'/pixelart/(\d+)\.htm'
		url = f"https://pixeljoint.com/pixels/profile_tab_icons.asp?id={self.id}&pg={page}"

		return re.findall(icons_pattern, HttpClient.get(url))

	def exists(self, directory: str) -> bool:
		"""
		Checks if the artist folder exists on the given directory.

		Arguments:
			directory: The target directory.
			format: The folder format.
		Returns:
			bool: If the directory exists or not.
		"""
		return os.path.isdir(f"{directory}/{self.id}_{self.name}")

	def create(self, directory: str) -> None:
		"""
		Creates a directory for the artist.

		Arguments:
			directory: The directory it is going to be created.
		"""
		os.mkdir(f"{directory}/{self.id}_{self.name}")