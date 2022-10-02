from .pyytdata import PyYtData
from .util import VidInfo


def vid_info(url: str) -> VidInfo:
    """Takes URL of the video and return the VidInfo object"""
    videoid = url.split("=")
    return VidInfo(videoid=videoid[-1])
