# youtube-api-wrapper
This is an youtube api v3 wrapper which is integrated in any python app basically in web app which recommend youtube videos
### this is a simple client for youtube data api v3 
## Prerequisites
Get the youtube data v3 api key from https://console.developers.google.com/apis/
Set environment variable API_KEY='Your YoutubeDatav3 API key'
and also GOOGLE_APPLICATION_CREDENTIALS='path/to/json/file'
Reference to set these environment variable 
https://cloud.google.com/docs/authentication/getting-started  
## Installation
Currently you add this package in python site-packages directories, global and per user.
Anyone can easily retrieve the  site-package directories by just firing the repl and running two commands
```
import sys
sys.path

```
mv the package to the site-package

## using
```python
import pyytdatav

p=pyytdata.PyYtData(keyword,maxlen) #keyword is the query you want to search from youtube data api and maxlen is no. of response you want

output=p.get_titles() #function call for titles of video
output=p.open_id(item_no) #function to open the specific video in web browser 

```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
