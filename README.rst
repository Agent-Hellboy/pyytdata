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
       pip install pyytdata

    for developement
       git clone https://github.com/Agent-Hellboy/YouTubeDataApi_Wrapper/
       cd flask-hedcrypt
       virtualenv venv
       source venv/bin/activate
       pip install -r requirements.txt
      

using
-----

.. code-block:: python

    from pyytdata.pyytdata import PyYtData

    >>> l=PyYtData('flask',1)
    >>> p=l.get_videoinfo()
    >>> dir(p)
    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    >>> p
    [<util.vidinfo.VidInfo object at 0x7ff971539e10>]
    >>> dir(p[0])
    ['_Info__API_KEY', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_id', 'channel_info', 'get_descriptions', 'get_image_urls', 'get_links', 'get_publishedtime', 'get_titles', 'keyword', 'maxlen', 'open_id', 'order', 'result', 'type', 'youtube']
    >>> c=p[0].channel_info()
    >>> dir(c)
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'id', 'result', 'total_subscriber', 'total_video', 'total_viewcnt', 'youtube']
    >>> c.total_viewcnt()
    '95246354'



General Info
------------
Under Developement
Please have a look at the Issue

Contributing
------------

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
