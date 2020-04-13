# youtube-api-wrapper
this is an youtube api v3 wrapper which is integrated in any python app basically in web app which recommend youtube videos
### this is a simple client for youtube data api v3 
## Prerequisites
get the youtube data v3 api key from https://console.developers.google.com/apis/
## Installation
currently you add this package in python site-packages directories, global and per user.
anyone can easily retrieve the  site-package directories following this
open yoru terminal and type python or python3
```python
prince@prince:~$ python3
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from distutils.sysconfig import get_python_lib
>>> print(get_python_lib())
/usr/lib/python3/dist-packages
# or
>>> import distutils
>>> distutils.__file__
'/usr/lib/python3.6/distutils/__init__.py'
>>> 

# or
prince@prince:~$ python3 -m site --user-site
/home/prince/.local/lib/python3.6/site-packages
# or
import sys; 
print [f for f in sys.path if f.endswith('packages')]
```
mv the package to the site-package

## using
```python
import pyytdatav3

p=pyytdatav3.PyYtData(keyword,maxlen) #keyword is the query you want to search from youtube data api and maxlen is no. of response you want

output=p.get_titles() #function call for titles of video
output=p.open_id(item_no) #function to open the specific video in web browser 

```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
