import requests
import os

class Artist():
	def __init__(self, name: str, _id: int):
		self.name = name
		self.id = _id

class Pixeljoint():

	def __init__(self, directory: str, _list: str, session: requests.Session):
		
		self.directory: str = directory
		
		self.list: str = _list
		
		self.session: requests.Session = session

	def parse_artist(url: str) -> Artist:
		"""
		Parses a Artist Object from a Artist URL.
		"""

	def parse_artist_icons(artist: Artist, page: int) -> list:
		"""
		Parses icons from a Artist (Object) on the given page.
		"""

	def parse_icon_image(id: int) -> str:
		"""
		Parses image URL from given icon id.
		"""

	def parse_image_name(url: str) -> str:
		"""
		Gets the image name from url.
		"""

	def create_folder(artist: Artist) -> None:
		"""
		Creates a Artist folder,
		using os.mkdir currently, could change in the future.
		"""

	def save_image(url: str, artist: Artist) -> None:
		"""
		Downloads the given image by URL on the Artist folder.
		Currently using wget, could change if needed.
		"""

	def image_exists(name: str) -> bool:
		"""
		Checks if the given image exists on the directory.
		"""

	def artist_exists(artist: Artist) -> bool:
		"""
		Check if artist folder exists.
		"""

	def start() -> None:
		"""
		Initializes the list scraping loop.
		"""
		page = 1
		
		for url in self.list:
			artist = self.parse_artist(url)
			icons = self.parse_artist_icons(artist, page)

			# Creates a artist folder on the directory
			# if the folder doesnt exists.
			if self.artist_exists(artist) == False:
				self.create_folder(artist)

			# Skips to the next artist if on the final page.
			if icons == None:
				continue

			else:

				for icon in icons:
					image = self.parse_icon_image(icon)

					# Skips to the next icon if the image exists.
					if self.image_exists(self.parse_image_name(image)):
						continue

					else:
						self.save_image(image, artist)
			
				page += 1