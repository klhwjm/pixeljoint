from pixeljoint.pixeljoint import Pixeljoint
import requests

# Session
session = requests.session()
session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.3"})

pj = Pixeljoint(path, list_, session)
pj.start()
