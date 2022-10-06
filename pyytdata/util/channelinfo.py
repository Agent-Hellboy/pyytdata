import os

from apiclient.discovery import build


class ChannelInfo:
    """
    Params:
        id: id of the channel
    """

    def __init__(self, channel_id: int):
        self.channel_id = channel_id
        self.__API_KEY = os.environ.get(
            "API_KEY"
        )  # link to get the api key is in readme file
        if not self.__API_KEY:
            print(self.__API_KEY)
            raise TypeError("You must have API_KEY set as an environment variable")
        youtube = build("youtube", "v3", developerKey=self.__API_KEY)
        self.youtube = youtube
        req = self.youtube.channels().list(part="statistics", id=self.channel_id)
        self.result = req.execute()

    def total_viewcount(self) -> int:
        """Return total views for the channel"""
        return self.result["items"][0]["statistics"]["viewCount"]

    def total_subscriber(self) -> int:
        """Return number of subscribers of the channel"""
        return self.result["items"][0]["statistics"]["subscriberCount"]

    def total_video(self) -> int:
        """Returns total number of the video uploaded by the channel"""
        return self.result["items"][0]["statistics"]["videoCount"]
