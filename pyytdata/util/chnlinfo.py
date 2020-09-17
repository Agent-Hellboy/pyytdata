import os

from apiclient.discovery import build


class ChnlInfo:
    """
    Params:
        id: id of the channel
    """

    def __init__(self, id):
        self.id = id
        try:
            self.__API_KEY = os.environ.get(
                "API_KEY"
            )  # link to get the api key is in readme file
        except Exception:
            raise TypeError("You must have API_KEY set as an environment variable")
        youtube = build("youtube", "v3", developerKey=self.__API_KEY)
        self.youtube = youtube
        req = self.youtube.channels().list(part="statistics", id=self.id)
        self.result = req.execute()

    def total_viewcnt(self):
        """Return total views for the channel"""
        return self.result["items"][0]["statistics"]["viewCount"]

    def total_subscriber(self):
        """Return number of subscribers of the channel"""
        return self.result["items"][0]["statistics"]["subscriberCount"]

    def total_video(self):
        """Returns total number of the video uploaded by the channel"""
        return self.result["items"][0]["statistics"]["videoCount"]
