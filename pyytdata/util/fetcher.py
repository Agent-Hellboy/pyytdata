import os
from abc import ABC, abstractmethod

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()


class DataFetcher(ABC):
    @abstractmethod
    def get_result(self):
        pass


class ChannelDataFetcher(DataFetcher):
    def __init__(self):
        if __API_KEY := os.environ.get("API_KEY"):
            self.youtube = build("youtube", "v3", developerKey=__API_KEY)
        else:
            raise TypeError("You must have API_KEY set as an environment variable")

    def get_result(self, part, channel_id, channel_name):
        if channel_id:
            req = self.youtube.channels().list(part=part, id=channel_id)
        else:
            req = self.youtube.channels().list(part=part, forUsername=channel_name)
        return req.execute()


class VideoDataFetcher(DataFetcher):
    qtype = None

    def __init__(self):
        if __API_KEY := os.environ.get("API_KEY"):
            self.youtube = build("youtube", "v3", developerKey=__API_KEY)
        else:
            raise TypeError("You must have API_KEY set as an environment variable")

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
