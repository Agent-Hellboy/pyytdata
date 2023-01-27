"""Contains a class PyYtData having implementation of youtube data v3 client"""
from typing import List

from .util.fetcher import VideoDataFetcher
from .util.info import VideoInfo


class PyYtData:
    """
    Class which acts as a client to the youtube data v3 API,
    having attributes as the query parameter for API.
    """

    def __init__(self, keyword: str, maxlen: int, type: str = "video") -> None:
        self.keyword = keyword
        self.maxlen = maxlen
        self.type = type

    def get_videoinfo(self) -> List:
        """Returns generator object of VideoInfo"""
        v = VideoDataFetcher()
        vid_info = VideoInfo(v, "snippet", keyword=self.keyword, maxlen=self.maxlen)
        for indx in range(self.maxlen):
            yield vid_info.get_info(indx)
