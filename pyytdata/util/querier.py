import os

from apiclient.discovery import build

from .info import Info


class VideoQuerier(Info):

    def __init__(
        self,
        keyword: str,
        maxlen: int,
        order: str = "relevance",
        videotype: str = "video",
        videoCategoryId: int = 27,
        videoid: str = None,
    ):
        super().__init__(order="relevance", type="video")
        self.keyword = keyword
        self.maxlen = maxlen
        self.order = order
        self.type = videotype
        self.id = videoid
        self.videoCategoryId = videoCategoryId
        self.result = self.fetch()

    def fetch(self):
        req = self.query_youtube()
        return req.execute()

    def get_result(self):
        return self.result

    def query_youtube(self):
        if self.keyword:
            req = self.youtube.search().list(
                q=self.keyword,
                part="snippet",
                maxResults=self.maxlen,
                type=self.type,
                order=self.order,
                videoCategoryId=self.videoCategoryId,
            )
        else:
            req = self.youtube.videos().list(part="snippet", id=self.id)
        return req

class VideoCommentQuerier:
    def __init__(self, idVideoComment):
        try:
            self.__API_KEY = os.environ.get(
                "API_KEY"
            )  # link to get the api key is in readme file
        except Exception:
            raise TypeError("You must have API_KEY set as an environment variable")
        youtube = build("youtube", "v3", developerKey=self.__API_KEY)
        self.youtube = youtube
        self.__id = idVideoComment

        request = youtube.commentThreads().list(part="snippet", videoId=self.__id)
        self.result = request.execute()

    def get_result(self):
        return self.result
