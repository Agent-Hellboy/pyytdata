import os
from apiclient.discovery import build

from util.info import Info


class ChnlInfo(Info):
    def __init__(self, id):
        self.id = id
        req = youtube.channels().list(
            part='statistics',
            id=self.id
        )
        self.result = req.execute()

    def total_viewcnt():
        return self.result['items'][0]['statistics']['viewCount']

    def total_subscriber():
        return self.result['items'][0]['statistics']['subscriberCount']

    def total_video():
        return self.result['items'][0]['statistics']['videoCount']
