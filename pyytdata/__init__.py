from .pyytdata import PyYtData
from .util import VidInfo


def vid_info(url):
    """
    Takes URL of the video and return the VidInfo object
    """
    id = url.split("=")
    return VidInfo(id=id[-1])
