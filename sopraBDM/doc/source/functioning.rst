###########
Functioning
###########

Our application can be used in two ways : frow a web browser, as a browsable API, or as web service from yur own application. We provide here the two ways to access it.

=============
Browsable API
=============

The API can be browsed from the URL of your localhost, on the port you specified : ``localhost:8000/api/``


=============
From terminal
=============

We provide here the way to query our API using python, from a terminal :

.. code-block:: python

    import requests
    import json

    r = requests.get("http://localhost:8000/api")
    r.content

    d = json.loads(r.content)

