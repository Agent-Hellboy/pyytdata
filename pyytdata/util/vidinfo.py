import os

from apiclient.discovery import build
from dateutil import parser

from .info import Info
from .channelinfo import ChannelInfo
from .querier import VideoCommentQuerier, VideoQuerier

VIDEO_CATEGORY = {
    "1": "Film & Animation",
    "2": "Cars & Vehicles",
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
        obj = VideoQuerier(self.keyword, self.maxlen, self.order, self.type, video_id= self.id)
        return obj.get_result()

    def __init__(
        self,
        type: str = None,
        keyword: str = None,
        maxlen: int = 3,
        indx: int = 0,
        video_id: str = None,
        order: str = "relevance",
    ):
        self._index = indx
        self.keyword = keyword
        self.maxlen = maxlen
        self.order = order
        self.type = type
        self.id = video_id
        self.result = self.__query_youtube("result")

    def get_title(self) -> str:
        """Returns title of the video"""
        return self.result["items"][self._index]["snippet"]["title"]

    def get_description(self) -> str:
        """Returns description of the video"""
        return self.result["items"][self._index]["snippet"]["description"]

    def get_image_url(self) -> str:
        """Returns url of the image"""
        return self.result["items"][self._index]["snippet"]["thumbnails"]["medium"][
            "url"
        ]

    def get_link(self) -> str:
        """Returns url of the video you can open using webbrower python module"""
        return (
            "https://www.youtube.com/watch?v="
            + self.result["items"][self._index]["id"]["videoId"]
        )

    def get_publisheddate(self):
        """Returns the date on which the video is published"""
        upload_date = parser.isoparse(
            self.result["items"][self._index]["snippet"]["publishTime"]
        )
        return upload_date.date()

    def get_channel_title(self) -> str:
        """Return the channel title"""
        return self.result["items"][self._index]["snippet"]["channelTitle"]

    def channel_stat(self):
        """Return channel object which has function to get stat of the channel"""
        channelStatId = self.result["items"][self._index]["snippet"]["channelId"]
        return ChannelInfo(channelStatId)

    def video_stat(self):
        statId = self.result["items"][self._index]["id"]["videoId"]
        return VidStat(statId)

    def comment_info(self):
        commentId = self.result["items"][self._index]["id"]["videoId"]
        return VidCmnt(commentId)


class VidStat:
    def __init__(self, id: int):
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

    def total_view(self) -> int:
        """Return number of views on the video"""
        return self.response["items"][0]["statistics"]["viewCount"]

    def total_like(self) -> int:
        """Return number of liks on the video"""
        return self.response["items"][0]["statistics"]["likeCount"]

    def total_dislike(self) -> int:
        """Return number of dislike on the video"""
        return self.response["items"][0]["statistics"]["dislikeCount"]

    def total_comment(self) -> int:
        """Return number of comments on the video"""
        return self.response["items"][0]["statistics"]["commentCount"]


class VidCmnt:
    def __query_youtube(self, name):
        if hasattr(self, name):
            return self.result
        obj = VideoCommentQuerier(self.id)
        return obj.get_result()

    def __init__(self, id: int):
        self.id = id
        self.result = self.__query_youtube("result")

    def total_comment(self) -> int:
        """Return total number of comments"""
        return self.result["pageInfo"]["totalResults"]

    def comment(self, vid_no: int) -> str:
        """Return the comment of that video number"""
        return self.result["items"][vid_no]["snippet"]["topLevelComment"]["snippet"][
            "textOriginal"
        ]

    def comment_author(self, vid_no: int) -> str:
        return self.result["items"][vid_no]["snippet"]["topLevelComment"]["snippet"][
            "authorDisplayName"
        ]

    def comment_author_channel_info(self, vid_no):
        # return self.result["items"][vid_no]["snippet"]["topLevelComment"]["snippet"][
        #     "authorChannelId"
        # ]["value"]
        pass
