"""Contains a class PyYtData having implementation of youtube data v3 client"""
from typing import List

from .util import VidInfo


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
        """Returns a list with has objects of VidInfo class"""
        for i in range(self.maxlen):
            yield VidInfo(self.type, self.keyword, self.maxlen, i)
