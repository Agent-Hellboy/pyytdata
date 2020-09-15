
from util.chnlinfo import ChnlInfo
from util.querier import VidQuerier
vido_catgy = {"2": "Cars & Vehicles",
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
              "44": "Trailers"
              }


class VidInfo():

  def __query_youtube(self, name):
    if hasattr(self, name):
      return self.result
    else:
      obj = VidQuerier(self.keyword, self.maxlen, self.order, self.type)
      return obj.get_result()

  def __init__(self, keyword, maxlen, id, order, type):
    self._id = id
    self.keyword = keyword
    self.maxlen = maxlen
    self.order = order
    self.type = type
    self.result = self.__query_youtube("result")

  def get_title(self):
    """Returns title of the video"""
    return self.result["items"][self._id]["snippet"]["title"]

  def get_description(self):
    """Returns description of the video"""
    return self.result["items"][self._id]["snippet"]["description"]

  def get_image_url(self):
    """Returns url of the image"""
    return self.result["items"][self._id]["snippet"]["thumbnails"]["medium"]["url"]

  def get_link(self):
    """Returns url of the video you can open using webbrower python module"""
    return "https://www.youtube.com/watch?v=" + self.result["items"][self._id]["id"]["videoId"]

  def get_publishedtime(self):
    pass

  def channel_info(self):
    """Return channel object which has function to get stat of the channel"""
    id = self.result["items"][self._id]["snippet"]["channelId"]
    return ChnlInfo(self.youtube, id)
