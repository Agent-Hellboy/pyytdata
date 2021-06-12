import os

from dateutil import parser
from apiclient.discovery import build

from .chnlinfo import ChnlInfo
from .querier import VidQuerier, VidCmntQuerier
from .info import Info

vido_catgy = {
    "2": "Cars & Vehicles",
    "1": "Film & Animation",
    "10": "Music",
    "15": "Pets & Animals",
    "17": "Sports",
    "18": "Short Movies",
    "19": "Travel & Events",
    "20": "Gaming",
    "21": "Videoblogging",
    "22": "People & Blogs",
    "23": "Comedy",
    "24": "Entertainment",
    "25": "News & Politics",
    "26": "Howto & Style",
    "27": "Education",
    "28": "Science & Technology",
    "29": "Nonprofits & Activism",
    "30": "Movies",
    "31": "Anime / Animation",
    "32": "Action / Adventure",
    "33": "Classics",
    "34": "Comedy",
    "35": "Documentary",
    "36": "Drama",
    "37": "Family",
    "38": "Foreign",
    "39": "Horror",
    "40'": "Sci - Fi / Fantasy",
    "41": "Thriller",
    "42": "Shorts",
    "43": "Shows",
    "44": "Trailers",
}


class VidInfo:
    def __query_youtube(self, name):
        if hasattr(self, name):
            return self.result
        else:
            obj = VidQuerier(self.keyword, self.maxlen, self.order, self.type, self.id)
            return obj.get_result()

    def __init__(
        self,
        type=None,
        keyword=None,
        maxlen=3,
        indx=0,
        id=None,
        order="relevance",
    ):
        self._indx = indx
        self.keyword = keyword
        self.maxlen = maxlen
        self.order = order
        self.type = type
        self.id = id
        self.result = self.__query_youtube("result")

    def get_title(self):
        """Returns title of the video"""
        return self.result["items"][self._indx]["snippet"]["title"]

    def get_description(self):
        """Returns description of the video"""
        return self.result["items"][self._indx]["snippet"]["description"]

    def get_image_url(self):
        """Returns url of the image"""
        return self.result["items"][self._indx]["snippet"]["thumbnails"]["medium"][
            "url"
        ]

    def get_link(self):
        """Returns url of the video you can open using webbrower python module"""
        return (
            "https://www.youtube.com/watch?v="
            + self.result["items"][self._indx]["id"]["videoId"]
        )

    def get_publisheddate(self):
        """Returns the date on which the video is published"""
        upload_date = parser.isoparse(
            self.result["items"][self._indx]["snippet"]["publishTime"]
        )
        return upload_date.date()

    def get_channel_title(self):
        """Return the channel title"""
        return self.result["items"][self._indx]["snippet"]["channelTitle"]

    def channel_stat(self):
        """Return channel object which has function to get stat of the channel"""
        id = self.result["items"][self._indx]["snippet"]["channelId"]
        return ChnlInfo(id)

    def video_stat(self):
        id = self.result["items"][self._indx]["id"]["videoId"]
        return VidStat(id)

    def comment_info(self):
        id = self.result["items"][self._indx]["id"]["videoId"]
        return VidCmnt(id)


class VidStat:
    def __init__(self, id):
        try:
            self.__API_KEY = os.environ.get(
                "API_KEY"
            )  # link to get the api key is in readme file
        except Exception:
            raise TypeError("You must have API_KEY set as an environment variable")
        youtube = build("youtube", "v3", developerKey=self.__API_KEY)
        self.youtube = youtube
        self._id = id
        request = self.youtube.videos().list(part="statistics", id=self._id)
        self.response = request.execute()

    def total_view(self):
        return self.response["items"][0]["statistics"]["viewCount"]

    def total_like(self):
        return self.response["items"][0]["statistics"]["likeCount"]

    def total_dislike(self):
        return self.response["items"][0]["statistics"]["dislikeCount"]

    def total_comment(self):
        return self.response["items"][0]["statistics"]["commentCount"]


class VidCmnt:
    def __query_youtube(self, name):
        if hasattr(self, name):
            return self.result
        else:
            obj = VidCmntQuerier(self.id)
            return obj.get_result()

    def __init__(self, id):
        self.id = id
        self.result = self.__query_youtube("result")

    def total_comment(self):
        return self.result["pageInfo"]["totalResults"]

    def comment(self, vid_no):
        return self.result["items"][vid_no]["snippet"]["topLevelComment"]["snippet"][
            "textOriginal"
        ]

    def comment_author(self, vid_no):
        return self.result["items"][vid_no]["snippet"]["topLevelComment"]["snippet"][
            "authorDisplayName"
        ]

    def comment_author_channel_info(self, vid_no):
        # return self.result["items"][vid_no]["snippet"]["topLevelComment"]["snippet"][
        #     "authorChannelId"
        # ]["value"]
        pass
