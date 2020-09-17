import json
import os
from apiclient.discovery import build
from dateutil import parser
youtube = build("youtube", "v3", developerKey=os.environ.get(
                "API_KEY"
                ))

# request = youtube.commentThreads().list(
#     part="snippet",
#     videoId="-biOGdYiF-I"
# )
# req = request.execute()

# print(req['pageInfo']['totalResults'])
# print(req['items'][0]['snippet']['topLevelComment']['snippet']['textOriginal'])
# print(req['items'][0]['snippet']['topLevelComment']['snippet']['authorDisplayName'])
# print(req['items'][0]['snippet']['topLevelComment']['snippet']['authorChannelId']['value'])

# request = youtube.videos().list(
#     part="statistics",
#     id="-biOGdYiF-I"
# )
# response = request.execute()
# print(response)
# print(response['items'][0]['statistics']['viewCount'])
# print(response['items'][0]['statistics']['likeCount'])
# print(response['items'][0]['statistics']['dislikeCount'])
# print(response['items'][0]['statistics']['commentCount'])

request = youtube.search().list(
    part="snippet",
    q="Jay Chou Mojito"
)
response = request.execute()

print(response['items'][0]['id']['videoId'])
