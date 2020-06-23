from util.info import Info

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


class VidInfo(Info):
  def __init__(self, keyword, maxlen, id, order="relevance", type="video", videoCategoryId=27):
    self.keyword = keyword
    self.maxlen = maxlen
    self.order = order
    self.type = type
    self._id = id
    super().__init__(keyword, maxlen, id, order="relevance", type="video")
    req = self.youtube.search().list(
        q=self.keyword,
        part="snippet",
        maxResults=self.maxlen,
        type=self.type,
        order=self.order,
        videoCategoryId=videoCategoryId
    )
    self.result = req.execute()

  def open_id(self):
    return "https://www.youtube.com/watch?v=" + self.result["items"][self._id]["id"]["videoId"]

  def get_titles(self):
    print(self._id)
    print(type(self._id))
    return self.result["items"][self._id]["snippet"]["title"]

  def get_descriptions(self):
    return self.result["items"][self._id]["snippet"]["description"]

  def get_image_urls(self):
    return self.result["items"][self._id]["snippet"]["thumbnails"]["medium"]["url"]

  def get_links(self):
    return "https://www.youtube.com/watch?v=" + self.result["items"][self._id]["id"]["videoId"]

  def get_publishedtime():
    pass

  def channel_info(self):
    id = self.result["items"][self._id]["id"]["videoId"]
    return ChnlInfo(id)
