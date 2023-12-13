import subprocess
import requests
import re
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

	def parse_artist(self, url: str) -> Artist:
		"""
		Parses a Artist Object from a Artist URL.
		"""
		name_pattern = r'<title>Pixel Artist - (.+)</title>'
		page_content = self.session.get(url).text
		match = re.search(name_pattern, page_content)

		_id = url.split('/')[-1].split('.')[0]

		return Artist(match[1], _id)

	def parse_artist_icons(self, artist: Artist, page: int) -> list:
		"""
		Parses icons from a Artist (Object) on the given page.
		"""
		icons_pattern = r'/pixelart/(\d+)\.htm'

		page_content = self.session.get(f"https://pixeljoint.com/pixels/profile_tab_icons.asp?id={artist.id}&pg={page}").text

		return re.findall(icons_pattern, page_content)

	def parse_icon_image(self, _id: int) -> str:
		"""
		Gets image URL from given icon id.
		"""
		image_pattern = r'<meta\s+property="og:image"\s+content="([^"]+)"\s*/>'

		page_content = self.session.get(f"https://pixeljoint.com/pixelart/{_id}.htm").text

		match = re.search(image_pattern, page_content)
		return match[1]

	def parse_image_name(self, url: str) -> str:
		"""
		Gets the image name from url.
		"""
		return url.split("/")[-1]

	def create_folder(self, artist: Artist) -> None:
		"""
		Creates the Artist folder.
		"""
		os.mkdir(f"{self.directory}/{artist.id}_{artist.name}")

	def save_image(self, url: str, artist: Artist) -> None:
		"""
		Downloads the given image by URL on the Artist folder.
		Currently using subprocess wget, could change if needed.
		"""
		subprocess.run(["wget", "-nv", "-P", f"{self.directory}/{artist.id}_{artist.name}", url], check=True)

	def image_exists(self, name: str, artist: Artist) -> bool:
		"""
		Checks if the image exists on the given artist folder.
		"""
		return os.path.exists(f"{self.directory}/{artist.id}_{artist.name}/{name}")

	def artist_exists(self, artist: Artist) -> bool:
		"""
		Check if artist folder exists.
		"""
		return os.path.isdir(f"{self.directory}/{artist.id}_{artist.name}")

	def start(self) -> None:
		"""
		Initializes the list scraping loop.
		"""

		page = 1
		for url in self.list:

			artist = self.parse_artist(url)
			print(f"Starting {artist.name} - {artist.id}")

			# Creates a artist folder on the directory
			# if the folder doesnt exists.
			if self.artist_exists(artist) == False:
				self.create_folder(artist)

			while True:
				icons = self.parse_artist_icons(artist, page)

				# Skips to the next artist if on the final page.
				if not icons:
					print(f"Finished {artist.name} - {artist.id}")
					break
				else:

					for icon in icons:
						image = self.parse_icon_image(icon)

						# Skips to the next icon if the image exists.
						if self.image_exists(self.parse_image_name(image), artist):
							continue
						else:
							self.save_image(image, artist)

					page += 1