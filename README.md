pyytdata
========

This is a youtube data api v3 wrapper which can be integrated into any
python app basically in the web app which recommends youtube videos.

[![image]][1]

[![image][2]][3]

[![image][4]][1]

[![image][5]][1]

[![image][6]][7]

[![image][8]][1]

[![image][9]][10]

Prerequisites
-------------

-   Get the youtube data v3 api key from
    <https://console.developers.google.com/apis/>
-   Set environment variable API\_KEY='Your YoutubeDatav3 API key'

Installation
------------

> for stable version
> -   pip install pyytdata
>
> for developement
> -   git clone
>     <https://github.com/Agent-Hellboy/YouTubeDataApi_Wrapper/>
> -   cd YouTubeDataApi\_Wrapper
> -   virtualenv venv
> -   source venv/bin/activate
> -   pip install -r requirements.txt

using
-----

    >>> from pyytdata.pyytdata import PyYtData
    >>> obj=PyYtData('flask',1)
    >>> vid=obj.get_videoinfo()
    >>> vid
    [<util.vidinfo.VidInfo object at 0x7ff971539e10>]

    #You can fire dir on this object to get the attribute and method of the object.
    >>> dir(vid[0])
    ['_Info__API_KEY', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_id', 'channel_info', 'get_description', 'get_image_url', 'get_link', 'get_publishedtime', 'get_title', 'keyword', 'maxlen', 'open_id', 'order', 'result', 'type', 'youtube']

    # To get the description of the video
    >>> vid[0].get_description()
    'Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. Learn how to use it ...'

    # To get the title of the video.
    >>> vid[0].get_title()
    'Learn Flask for Python - Full Tutorial'

    # To get the link for the video which can we used in web app to open the link for the video.
    >>> vid[0].get_link()
    'https://www.youtube.com/watch?v=Z1RJmh_OqeA'

    # To get the title img of the video which can be rend

  [image]: https://img.shields.io/pypi/v/pyytdata
  [1]: https://pypi.python.org/pypi/pyytdata/
  [2]: https://travis-ci.org/Agent-Hellboy/YouTubeDataApi_Wrapper.svg?branch=master
  [3]: https://travis-ci.org/Agent-Hellboy/YouTubeDataApi_Wrapper
  [4]: https://img.shields.io/pypi/pyversions/pyytdata.svg
  [5]: https://img.shields.io/pypi/l/pyytdata.svg
  [6]: https://pepy.tech/badge/pyytdata
  [7]: https://pepy.tech/project/pyytdata
  [8]: https://img.shields.io/pypi/format/pyytdata.svg
  [9]: https://coveralls.io/repos/github/Agent-Hellboy/YouTubeDataApi_Wrapper/badge.svg?branch=master
  [10]: https://coveralls.io/github/Agent-Hellboy/YouTubeDataApi_Wrapper?branch=master
