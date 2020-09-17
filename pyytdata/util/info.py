import os
from apiclient.discovery import build


class Info:
    """
    Class which acts as a client to the youtube data v3 API,
    having attributes as the query parameter for API.
    """

    def __init__(self, keyword, maxlen, order="relevance", type="video"):
        try:
            self.__API_KEY = os.environ.get(
                "API_KEY"
            )  # link to get the api key is in readme file
        except Exception:
            raise TypeError("You must have API_KEY set as an environment variable")
        youtube = build("youtube", "v3", developerKey=self.__API_KEY)
        self.youtube = youtube
