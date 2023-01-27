from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class YtChannelStat:
    total_viewcount: int
    total_subscriber: int
    total_video: int


@dataclass(frozen=True)
class YtVideoStat:
    total_view: int
    total_like: int
    fav_count: int
    total_comment: int


@dataclass(frozen=True)
class YtChannelInfo:
    title: str
    description: str


@dataclass(frozen=True)
class YtVideoInfo:
    title: str
    description: str
    image_url: str
    link: str
    publisheddate: datetime
    channel_title: str
