"""
Contains a class PyYtData having implementation of youtube data v3 client.
"""

import os
import webbrowser
import json

from apiclient.discovery import build

from .util import VidInfo


class PyYtData:
    """
    Class which acts as a client to the youtube data v3 API,
    having attributes as the query parameter for API.
    """

    def __init__(self, keyword, maxlen, order="relevance", type="video"):
        self.keyword = keyword
        self.order = order
        self.maxlen = maxlen
        self.type = type

    def get_videoinfo(self):
        """Returns a list with has objects of VidInfo class"""
        rslt = []

        for i in range(self.maxlen):
            vid = VidInfo(self.keyword, self.maxlen, i, self.order, self.type)
            rslt.append(vid)
        return rslt
