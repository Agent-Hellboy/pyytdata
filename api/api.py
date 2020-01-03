import webbrowser
from apiclient.discovery import build      
class API:
	def __init__(self,keyword,maxlen):
		self._api_key=YOU YOUTUBE DATA V3 API KEY
		#link to get the api key is in readme file
		youtube=build('youtube','v3',developerKey=self._api_key)
		self.keyword=keyword
		self.maxlen=maxlen
		req=youtube.search().list(q=self.keyword,part='snippet',type='video',maxResults=self.maxlen)
		self.result=req.execute() 
	def open_id(self,item_no):
		return webbrowser.open('https://www.youtube.com/watch?v='+self.result['items'][item_no]['id']['videoId'])
	def get_titles(self):
		stm=[]
		for i in range(self.maxlen):
			stm.append(self.result['items'][i]['snippet']['title'])
		return stm
	def get_descriptions(self):
		stm=[]
		for i in range(self.maxlen):
			stm.append(self.result['items'][i]['snippet']['description'])
		return stm
	def get_image_urls(self):
		stm=[]
		for i in range(self.maxlen):
			stm.append(self.result['items'][0]['snippet']['thumbnails']['medium']['url'])
		return stm
		
		
