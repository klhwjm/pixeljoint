from pixeljoint.artist import Artist
from pixeljoint.archive import Archive
from pixeljoint.icon import Icon
from pixeljoint.misc import Misc

class Pixeljoint():
	"""
	This class is the root class that is responsible
	for the main scraping.
	"""
	def __init__(self, directory: str, _list: str, archive: str):
		self.directory: str = directory
		
		with open(_list, "r", encoding="utf-8") as f:
			self.list = f.read().splitlines()

		self.archive: str = archive

	def start(self):
		"""
		Starts the main scraping of the profile list.
		"""
		archive = Archive.load(self.archive)

		# Loops trough all the profiles on the given list.
		for url in self.list:
			page = 1

			# Parses the artist information from the profile url.
			artist = Artist.parse(url)

			print(f"Starting {artist.name} - {artist.id}")

			# Creates the artist folder in case it doesnt exists.
			if not artist.exists(self.directory):
				artist.create(self.directory)

			# Start looping trough the icons pages.
			while True:
				# Parses the artist icons.
				icons = artist.icons(page)

				# If there arent more icons, break the loop.
				if not icons:
					print(f"Finished {artist.name} - {artist.id}")
					break

				# If there is icons on the page, loop trough them.
				for icon in icons:

					# If the icon id is on the archive, go to the next icon.
					if archive.exists(icon):
						continue
					# If is not.
					else:
						# Parse the icon image.
						image = Icon.parse(icon)

						# Download the image.
						Misc.save(image.url, f"{self.directory}/{artist.id}_{artist.name}")

						# Write it on the archive.
						archive.write(icon)

				# Increase page counting.
				page += 1
