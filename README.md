# youtube-api-wrapper
this is an youtube api v3 wrapper which is integrated in any python app basically in web app which recommend youtube videos
### this is a simple client for youtube data api v3  It uses Youtube Data API v3.

## Installation
currently you add this package in python site-packages directories, global and per user.

## using
```python
import api

p=api.API(keyword,maxlen) #keyword is the query you want to search from youtube data api and maxlen is no. of response you want

p.get_titles() #function call for titles of video
p.open_id(item_no) #function to open the specific video in web browser 

```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
