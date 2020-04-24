"""
pyytdata file.

"""
import os
import webbrowser

from apiclient.discovery import build


class PyYtData:
	"""
	
	"""
	@staticmethod
	def _get_api_key():
		api_key=os.environ.get("API_KEY")
		auth_verfy=os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
		if api_key == None or auth_verfy == None:
			raise ValueError("environment variable API_KEY and GOOGLE_APPLICATION_CREDENTIALS is not set")
		return api_key
		
	def __init__(self, keyword, maxlen):
		self._API_KEY = PyYtData._get_api_key() 
		print(self._API_KEY)
		youtube = build("youtube", "v3", developerKey=self._API_KEY)
		self.keyword = keyword
		self.maxlen = maxlen
		req = youtube.search().list(
			q=self.keyword, part="snippet", type="video", maxResults=self.maxlen
		)
		self.result = req.execute()

	def open_id(self, item_no):
		return webbrowser.open(
			"https://www.youtube.com/watch?v="
			+ self.result["items"][item_no]["id"]["videoId"]
			)

	def get_titles(self):
		rslt = []
		for i in range(self.maxlen):
			rslt.append(self.result["items"][i]["snippet"]["title"])
		return rslt

	def get_descriptions(self):
		rslt = []
		for i in range(self.maxlen):
			rslt.append(self.result["items"][i]["snippet"]["description"])
		return rslt

	def get_image_urls(self):
		rslt = []
		for i in range(self.maxlen):
			rslt.append(
			self.result["items"][0]["snippet"]["thumbnails"]["medium"]["url"]
		)
		return rslt
		
		
