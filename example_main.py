from pixeljoint.pixeljoint import Pixeljoint
import requests

# Session
session = requests.session()
session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.3"})

# List
with open("list.txt", "r", encoding="utf-8") as f:
	_list = f.read().splitlines()

pj = Pixeljoint("/home/avoid/pixeljoint/artists", _list, session)
pj.start()