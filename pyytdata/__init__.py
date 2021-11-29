from .pyytdata import PyYtData

from .util import VidInfo


def vid_info(url: str) -> VidInfo:
    """Takes URL of the video and return the VidInfo object"""
    id = url.split("=")
    return VidInfo(id=id[-1])
