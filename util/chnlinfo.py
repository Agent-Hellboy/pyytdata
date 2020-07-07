import os
from apiclient.discovery import build
from util.info import Info


class ChnlInfo(Info):
    def __init__(self, youtube, id):
        self.id = id
        self.youtube = youtube
        req = self.youtube.channels().list(
            part='statistics',
            id=self.id
        )
        self.result = req.execute()

    def total_viewcnt(self):
        return self.result['items'][0]['statistics']['viewCount']

    def total_subscriber(self):
        return self.result['items'][0]['statistics']['subscriberCount']

    def total_video(self):
        return self.result['items'][0]['statistics']['videoCount']
