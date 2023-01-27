import os
from abc import ABC, abstractmethod

from googleapiclient.discovery import build


class DataFetcher(ABC):
    def __init__(self):
        __API_KEY = os.environ.get("API_KEY")
        if not __API_KEY:
            raise TypeError("You must have API_KEY set as an environment variable")
        self.youtube = build("youtube", "v3", developerKey=__API_KEY)

    @abstractmethod
    def get_result(self):
        """Fetch Result from YouTube Data v3 API using googleapiclinet"""


class ChannelDataFetcher(DataFetcher):
    def __init__(self):
        super().__init__()

    def get_result(self, part, channel_id, channel_name):
        if channel_id:
            req = self.youtube.channels().list(part=part, id=channel_id)
        else:
            req = self.youtube.channels().list(part=part, forUsername=channel_name)
        return req.execute()


class VideoDataFetcher(DataFetcher):
    qtype = None

    def __init__(self):
        super().__init__()

    def get_result(
        self,
        part,
        maxlen,
        keyword=None,
        video_id=None,
        video_category_id=27,
        order="relevance",
    ):
        if video_id:
            req = self.youtube.videos().list(part=part, id=video_id)
            self.qtype = "list"
        else:
            req = self.youtube.search().list(
                q=keyword,
                part=part,
                maxResults=maxlen,
                type="video",
                order=order,
                videoCategoryId=video_category_id,
            )
            self.qtype = "search"
        return req.execute()
