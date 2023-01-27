pyytdata
========

A python library which provides metadata of YouTube videos.

.. image:: https://img.shields.io/pypi/v/pyytdata
   :target: https://pypi.python.org/pypi/pyytdata/

.. image:: https://github.com/Agent-Hellboy/YouTubeDataApi_Wrapper/actions/workflows/build.yml/badge.svg
    :target: https://github.com/Agent-Hellboy/YouTubeDataApi_Wrapper/

.. image:: https://github.com/Agent-Hellboy/YouTubeDataApi_Wrapper/actions/workflows/lint.yml/badge.svg
    :target: https://github.com/Agent-Hellboy/YouTubeDataApi_Wrapper/

.. image:: https://img.shields.io/pypi/pyversions/pyytdata.svg
   :target: https://pypi.python.org/pypi/pyytdata/

.. image:: https://img.shields.io/pypi/l/pyytdata.svg
   :target: https://pypi.python.org/pypi/pyytdata/

.. image:: https://pepy.tech/badge/pyytdata
   :target: https://pepy.tech/project/pyytdata

.. image:: https://img.shields.io/pypi/format/pyytdata.svg
   :target: https://pypi.python.org/pypi/pyytdata/

.. image:: https://coveralls.io/repos/github/Agent-Hellboy/pyytdata/badge.svg?branch=master
   :target: https://coveralls.io/github/Agent-Hellboy/pyytdata?branch=master


Prerequisites
-------------

- Get the youtube data v3 api key from https://console.developers.google.com/apis/
- Set environment variable API\_KEY='Your YoutubeDatav3 API key'


Installation
------------

    for stable version
       - pip install pyytdata

    for current_version
       - pip install git+https://github.com/Agent-Hellboy/pyytdata.git


Using
-----

   Public APIs
   
    - get_vid_info_from_url -> Return Video Info from URL
    - get_video_info -> Return Video Info from video_id
    - get_channel_info -> Return Channel Info from channel name
    - get_channel_stat_by_name -> Return channel stat from channel name
    - get_video_stat_by_ID -> Return Video stat from vide_id

Other APIs

.. code-block:: python

    >>> from pyytdata import PyYtData
    >>> obj=PyYtData('flask',1)
    >>> vid=obj.get_videoinfo()


General Info
------------
python-client for
https://developers.google.com/youtube/v3/docs/channels


Contributing
------------

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
