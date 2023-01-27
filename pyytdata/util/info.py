from abc import ABC, abstractmethod

from dateutil import parser

from pyytdata.util.ytdata import (
    YtChannelInfo, YtChannelStat, YtVideoInfo, YtVideoStat
)


class Info(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class VideoInfo(Info):
    def __init__(self, data_v3_api_obj, part, video_id=None, keyword=None, maxlen=5):
        self.data_v3_api_obj = data_v3_api_obj
        self.result = data_v3_api_obj.get_result(
            part, maxlen, video_id=video_id, keyword=keyword
        )

    def get_data(self, indx):
        video_data = self.result["items"][indx]["snippet"]
        self.title = video_data["title"]
        self.get_description = video_data["description"]
        self.image_url = video_data["thumbnails"]["medium"]["url"]
        vid_id = (
            self.result["items"][indx]["id"]
            if self.data_v3_api_obj.qtype == "list"
            else self.result["items"][indx]["id"]["videoId"]
        )
        self.link = f"https://www.youtube.com/watch?v={vid_id}"
        self.publisheddate = video_data["publishedAt"]
        # self.publisheddate = parser.isoparse(video_data["publishedAt"]).date()
        self.channel_title = video_data["channelTitle"]

    def get_info(self, idx):
        self.get_data(idx)
        return YtVideoInfo(
            title=self.title,
            description=self.get_description,
            image_url=self.image_url,
            link=self.link,
            publisheddate=self.publisheddate,
            channel_title=self.channel_title,
        )


class ChannelInfo(Info):
    def __init__(
        self, data_v3_api_obj, part, channel_id: int = None, channel_name: str = None
    ):
        self.result = data_v3_api_obj.get_result(part, channel_id, channel_name)


    def get_data(self):
        self.title = self.result["items"][0]["snippet"]["title"]
        self.description = self.result["items"][0]["snippet"]["description"]

    def get_info(self):
        self.get_data()
        return YtChannelInfo(title=self.title, description=self.description)


class VideoStatInfo(Info):
    def __init__(self, data_v3_api_obj, part, video_id, maxlen=5):
        self.response = data_v3_api_obj.get_result(part, maxlen, video_id=video_id)

    def get_data(self):
        stat_data = self.response["items"][0]["statistics"]
        self.total_view = stat_data["viewCount"]
        self.total_like = stat_data["likeCount"]
        self.total_fav = stat_data["favoriteCount"]
        self.total_comment = stat_data["commentCount"]

    def get_info(self):
        self.get_data()
        return YtVideoStat(
            total_view=self.total_view,
            total_like=self.total_like,
            fav_count=self.total_fav,
            total_comment=self.total_comment,
        )


class ChannelStatInfo(Info):
    def __init__(
        self, data_v3_api_obj, part, channel_id: int = None, channel_name: str = None
    ):
        self.result = data_v3_api_obj.get_result(part, channel_id, channel_name)

    def get_data(self):
        chnl_stat = self.result["items"][0]["statistics"]
        self.total_viewcount = chnl_stat["viewCount"]
        self.total_subscriber = chnl_stat["subscriberCount"]
        self.total_video = chnl_stat["videoCount"]

    def get_info(self):
        self.get_data()
        return YtChannelStat(
            total_viewcount=self.total_viewcount,
            total_subscriber=self.total_subscriber,
            total_video=self.total_video,
        )
