import os

from apiclient.discovery import build

from util.info import Info


class ChnlInfo(Info):
    """
    Params:
        youtube: youtube object to query the API
        id: id of the channel
    """

    def __init__(self, youtube, id):
        self.id = id
        self.youtube = youtube
        req = self.youtube.channels().list(
            part='statistics',
            id=self.id
        )
        self.result = req.execute()

    def total_viewcnt(self):
        """Return total views for the channel"""
        return self.result['items'][0]['statistics']['viewCount']

    def total_subscriber(self):
        """Return number of subscribers of the channel"""
        return self.result['items'][0]['statistics']['subscriberCount']

    def total_video(self):
        """Returns total number of the video uploaded by the channel"""
        return self.result['items'][0]['statistics']['videoCount']
