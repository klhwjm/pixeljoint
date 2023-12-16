import requests

class HttpClient():
	"""
	This class represents a HTTP Client,
	used as a root of HTTP Connections on the code.
	"""
	@staticmethod
	def get(url: str) -> str:
		"""
		Performs a GET Request to the URL and return its text.

		Arguments:
			url: The target URL.
		Returns:
			str: Response text.
		"""
		user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.3"}
		return requests.get(url, headers=user_agent).text