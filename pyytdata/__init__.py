from .pyytdata import PyYtData
from .util import VidInfo


def vid_info(url: str) -> VidInfo:
    """Takes URL of the video and return the VidInfo object"""
    video_id = url.split("=")
    return VidInfo(video_id=video_id[-1])
