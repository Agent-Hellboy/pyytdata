pyytdata
========

A python library which provides metadata of YouTube videos.

.. image:: https://img.shields.io/pypi/v/pyytdata
   :target: https://pypi.python.org/pypi/pyytdata/

.. image:: https://github.com/Agent-Hellboy/YouTubeDataApi_Wrapper/actions/workflows/build.yml/badge.svg
    :target: https://github.com/Agent-Hellboy/YouTubeDataApi_Wrapper/

.. image:: https://img.shields.io/pypi/pyversions/pyytdata.svg
   :target: https://pypi.python.org/pypi/pyytdata/

.. image:: https://img.shields.io/pypi/l/pyytdata.svg
   :target: https://pypi.python.org/pypi/pyytdata/

.. image:: https://pepy.tech/badge/pyytdata
   :target: https://pepy.tech/project/pyytdata

.. image:: https://img.shields.io/pypi/format/pyytdata.svg
   :target: https://pypi.python.org/pypi/pyytdata/

.. image:: https://coveralls.io/repos/github/Agent-Hellboy/pyytdata/badge.svg
   :target: https://coveralls.io/github/Agent-Hellboy/pyytdata

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
       - python -m venv .venv
       - source .venv/bin/activate
       - pip install -r requirements.txt


Using
-----

   Maybe the first step toward moving the package from a Toy package to a usable package.

   An API which will take the URL of youtube video and provide metadata of the video and the channel which has uploaded that video .

.. code-block:: python

   >>> from pyytdata import vid_info
   >>> l=vid_info('https://www.youtube.com/watch?v=0fqHuIqkOak')
   >>> l.get_title()
   'Manoj Bajpayee Vs. Atul Khatri | Epic Middle class Face-off | The Family Man | Amazon Prime Video'
   l is a VidInfo object

.. code-block:: python


    >>> from pyytdata import PyYtData
    >>> obj=PyYtData('flask',1)
    >>> vid=obj.get_videoinfo()
    >>> vid
    <generator object PyYtData.get_videoinfo at 0x7fb0f69f8040>

    #Since get_videoinfo returns a generator, you can either iterate or get the next() item.

    #You can fire dir on this object to get the attribute and method of the object.
    >>> dir(next(vid))
    ['_Info__API_KEY', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_id', 'channel_info', 'get_description', 'get_image_url', 'get_link', 'get_publishedtime', 'get_title', 'keyword', 'maxlen', 'open_id', 'order', 'result', 'type', 'youtube']

For more examples refer to the `\docs` folder

General Info
------------
Under Developement

.. image:: /images/info.png
   :width: 600

- I think the package has implemented the facade pattern as the lower level packages like videoinfo and chnlinfo are independent from pyytdata and is not exposed to client and also the interaction between querier and videoinfo is hidden from client by providing a interface/module pyytdata
- vidoinfo class and Chnlinfo has composition relationship as video does not exists without a channel



Contributing
------------

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Documentation
-------------

To see Documentation open the html files which are included in `docs/build/html/` directory. 

If anyone is interested in contributing to Documentation, 
they can make changes in the .rst files included in the `docs/source/` directory and 
then run `make html` in the `docs/`` directory.
