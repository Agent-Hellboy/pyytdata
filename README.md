# YouTubeDataApi_Wrapper 
This is an youtube api v3 wrapper which is integrated in any python app basically in web app which recommend youtube videos
### A simple client for youtube data api v3 


## Demo
![Watch the video](https://www.youtube.com/watch?v=dXt98TgGYng)

## Prerequisites
Get the youtube data v3 api key from https://console.developers.google.com/apis/
Set environment variable API_KEY='Your YoutubeDatav3 API key' </br>
and also GOOGLE_APPLICATION_CREDENTIALS='path/to/json/file' </br>
Reference to set GOOGLE_APPLICATION_CREDENTIALS
https://cloud.google.com/docs/authentication/getting-started  

## Installation
	
	   pip install pyytdata 

## using

       
        import pyytdatav

        p=pyytdata.PyYtData(keyword,maxlen) # keyword is the query you want to search from 
					    # youtube data api and maxlen is no. of video you want.
													

        output=p.get_titles() #function call for titles of video
        output=p.open_id(item_no) #function to open the specific video in web browser 



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

