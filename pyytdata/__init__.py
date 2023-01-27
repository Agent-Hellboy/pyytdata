from enum import Enum

from .pyytdata import PyYtData
from .util import (
    ChannelDataFetcher,
    ChannelInfo,
    ChannelStatInfo,
    VideoDataFetcher,
    VideoInfo,
    VideoStatInfo,
    YtChannelInfo,
    YtChannelStat,
    YtVideoInfo,
    YtVideoStat,
)


class VIDEO_CATEGORY(Enum):
    FILM_AND_ANIMATION = 1
    CARS_AND_VEHICLES = 2
    MUSIC = 10
    PETS_AND_ANIMALS = 15
    SPORTS = 17
    SHORT_AND_MOVIES = 18
    TRAVEL_AND_EVENTS = 19
    GAMING = 20
    VIDEOBLOGGING = 21
    PEOPLE_AND_BLOGS = 22
    ENTERTAINMENT = 24
    NEWS_AND_POLITICS = 25
    HOW_TO_STTYLE = 26
    EDUCATION = 27
    SCIENCE_AND_TECHNOLOGY = 28
    NONPROFITS_AND_ACTIVISM = 29
    MOVIES = 30
    ANIME_AND_ANIMATION = 31
    ACTION_AND_ADVENTURE = 32
    CLASSICS = 33
    COMEDY = 34
    DOCUMENTARY = 35
    DRAMA = 36
    FAMILY = 37
    FOREIGN = 38
    HORROR = 39
    SCIFI_AND_FANTASY = 40
    THRILLER = 41
    SHORTS = 42
    SHOWS = 43
    TRAILERS = 44


def get_vid_info_from_url(url: str) -> YtVideoInfo:
    """Return Video Info of given Video URL"""
    video_id = url.split("=")
    video_fetcher = VideoDataFetcher()
    vid_info = VideoInfo(video_fetcher, "snippet", video_id=video_id[-1])
    return vid_info.get_info(0)


def get_video_info(video_id: str) -> YtVideoInfo:
    """Return Video Info of video_id"""
    video_fetcher = VideoDataFetcher()
    vid_info = VideoInfo(video_fetcher, "snippet", video_id=video_id)
    return vid_info.get_info(0)


def get_channel_info(channel_name: str) -> YtChannelInfo:
    """Return Channel Info of channel_name"""
    channel_fetcher = ChannelDataFetcher()
    chnlinfo = ChannelInfo(channel_fetcher, "snippet", channel_name=channel_name)
    return chnlinfo.get_info()


def get_channel_stat_by_name(channel_name) -> YtChannelStat:
    """Return Channel Stat of channel_name"""
    channel_fetcher = ChannelDataFetcher()
    chnlinfo = ChannelStatInfo(channel_fetcher, "statistics", channel_name=channel_name)
    return chnlinfo.get_info()


def get_video_stat_by_ID(video_id: str) -> YtVideoStat:
    """Return Video Stat of channel_name"""
    video_fetcher = VideoDataFetcher()
    vid_stat = VideoStatInfo(video_fetcher, "statistics", video_id)
    return vid_stat.get_info()
