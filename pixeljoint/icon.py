from pixeljoint.httpclient import HttpClient
import re

class Image():
	def __init__(self, url: str):
		self.url: str = url
		self.filename = url.split("/")[-1]

class Icon():
	@staticmethod
	def parse(_id: int) -> Image:
		"""
		Parses a icon image from id and returns a Image object.

		Arguments:
			_id: The icon id.
		Returns:
			Image: The image object.
		"""
		image_pattern = r'<meta\s+property="og:image"\s+content="([^"]+)"\s*/>'
		url = f"https://pixeljoint.com/pixelart/{_id}.htm"

		match = re.search(image_pattern, HttpClient.get(url))
		
		return Image(match[1])