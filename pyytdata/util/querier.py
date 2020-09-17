from .info import Info


class VidQuerier(Info):
    def __init__(self, keyword, maxlen, order="relevance", type="video", videoCategoryId=27):
        self.keyword = keyword
        self.maxlen = maxlen
        self.order = order
        self.type = type
        super().__init__(keyword, maxlen, order="relevance", type="video")
        req = self.youtube.search().list(
            q=self.keyword,
            part="snippet",
            maxResults=self.maxlen,
            type=self.type,
            order=self.order,
            videoCategoryId=videoCategoryId
        )
        self.result = req.execute()

    def get_result(self):
        return self.result
