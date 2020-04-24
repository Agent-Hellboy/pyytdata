"""
pyytdata file.

""""
import os

import webbrowser
from apiclient.discovery import build


class PyYtData:
	"""
	
	"""
	@staticmethod
	def _get_api_key():
		api_key=os.environ.get("API_KEY") 
		if api_key == None:
			raise ValueError("no environment variable name API_KEY is found")
		
	def __init__(self, keyword, maxlen):
		self._API_KEY =self._get_api_key() 
		youtube = build("youtube", "v3", developerKey=self._API_KEY)
		self.keyword = keywor
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
		
		
