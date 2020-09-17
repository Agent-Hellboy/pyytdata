import json
import os
from apiclient.discovery import build
from dateutil import parser
youtube = build("youtube", "v3", developerKey=os.environ.get(
                "API_KEY"
                ))
req = youtube.search().list(
    q="flask",
    part="snippet",
    maxResults=4,
    type="video",
    order="relevance",
    videoCategoryId=27)
result = req.execute()
l = parser.isoparse(result['items'][0]["snippet"]["publishTime"])
print(l.date())
