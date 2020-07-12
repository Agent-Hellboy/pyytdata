pyytdata
========

This is an youtube api v3 wrapper which is integrated in any python app
basically in web app which recommend youtube videos

.. image:: https://img.shields.io/pypi/v/pyytdata
   :target: https://pypi.python.org/pypi/pyytdata/

.. image:: https://travis-ci.org/Agent-Hellboy/YouTubeDataApi_Wrapper.svg?branch=master
    :target: https://travis-ci.org/Agent-Hellboy/YouTubeDataApi_Wrapper

.. image:: https://img.shields.io/pypi/pyversions/pyytdata.svg
   :target: https://pypi.python.org/pypi/pyytdata/

.. image:: https://img.shields.io/pypi/l/pyytdata.svg
   :target: https://pypi.python.org/pypi/pyytdata/

.. image:: https://pepy.tech/badge/pyytdata
   :target: https://pepy.tech/project/pyytdata

.. image:: https://img.shields.io/pypi/format/pyytdata.svg
   :target: https://pypi.python.org/pypi/pyytdata/

.. image:: https://coveralls.io/repos/github/Agent-Hellboy/YouTubeDataApi_Wrapper/badge.svg?branch=master
   :target: https://coveralls.io/github/Agent-Hellboy/YouTubeDataApi_Wrapper?branch=master




Prerequisites
-------------

- Get the youtube data v3 api key from https://console.developers.google.com/apis/
- Set environment variable API\_KEY='Your YoutubeDatav3 API key'


Installation
------------

    for stable version
       - pip install pyytdata

    for developement
       - git clone https://github.com/Agent-Hellboy/YouTubeDataApi_Wrapper/
       - cd YouTubeDataApi_Wrapper
       - virtualenv venv
       - source venv/bin/activate
       - pip install -r requirements.txt
      

using
-----

.. code-block:: python

    from pyytdata.pyytdata import PyYtData

    >>> obj=PyYtData('flask',1)
    >>> vid=obj.get_videoinfo()
    >>> vid
    [<util.vidinfo.VidInfo object at 0x7ff971539e10>]
    
    You can fire dir on this object to get the attribute and method of the object.
    >>> dir(vid[0])
['_Info__API_KEY', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_id', 'channel_info', 'get_description', 'get_image_url', 'get_link', 'get_publishedtime', 'get_title', 'keyword', 'maxlen', 'open_id', 'order', 'result', 'type', 'youtube']

    
    To get the description of the video
    >>> vid[0].get_description()
    'Flask is a micro web framework written in Python. It is    classified as a microframework because it does not require particular tools or libraries. Learn how to use it ...'
    
    To get the title of the video.
    >>> vid[0].get_title()
'Learn Flask for Python - Full Tutorial'

    To get the link for the video which can we used in web app to open the link for the video.
    >>> vid[0].get_link()
'https://www.youtube.com/watch?v=Z1RJmh_OqeA'

    To get the title img of the video which can be rendered through HTML tag.
    >>> vid[0].get_image_url()
'https://i.ytimg.com/vi/Z1RJmh_OqeA/mqdefault.jpg'




    
    To get the chnlInfo object having methods which describes a channel.
    >>> chnl=vid[0].channel_info()
    To get the number of view cnt on this channel
    >>> dir(chnl)
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',  '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'id', 'result', 'total_subscriber', 'total_video', 'total_viewcnt', 'youtube']

    To get the total view count of the channel.
    >>> chnl.total_viewcnt()
    '95246354'
    
    To get the number of subscribers of the channel.
    >>> chnl.total_subscriber()
    '2170000'

    To get number of video uploaded by this particular channel.
    >>> chnl.total_video()
    '1133'

    


General Info
------------
Under Developement
Please have a look at the Issue

Contributing
------------

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
