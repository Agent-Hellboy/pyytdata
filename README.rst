pyytdata
========

|Version|

.. |Version| image:: https://img.shields.io/pypi/v/pyytdata
   :target: https://pypi.python.org/pypi/pyytdata/

This is an youtube api v3 wrapper which is integrated in any python app
basically in web app which recommend youtube videos 


Demo
----

.. figure:: pyytdata.gif
   :alt: PyYtData demo

  
Prerequisites
-------------

Get the youtube data v3 api key from
https://console.developers.google.com/apis/ Set environment variable
API\_KEY='Your YoutubeDatav3 API key' and also
GOOGLE\_APPLICATION\_CREDENTIALS='path/to/json/file' Reference to set
GOOGLE\_APPLICATION\_CREDENTIALS
https://cloud.google.com/docs/authentication/getting-started

Installation
------------

::

       pip install pyytdata 

using
-----

::

        from pyytdata import pyytdata
        # keyword is the query you want to search from 
        # youtube data api and maxlen is no. of video you want.
        
        p=pyytdata.PyYtData(keyword,maxlen) 
                                                    
        #function call for titles of video
        
        output=p.get_titles() 

        #function to open the specific video in web browser
        
        output=p.open_id(item_no)  

General Info
------------

Have a look at the example to get acquaint with the use cases.

Contributing
------------

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
