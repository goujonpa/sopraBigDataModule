#########
API Guide
#########

This section describres the different implemented requests.

==============
Get the models
==============

Example :

.. code-block:: python

    >>> import requests
    >>> import json

    >>> r = requests.get("http://localhost:8000/api/notations")

Gives

.. code-block:: python

    {
        "count": 32372,
        "next": "http://localhost:8000/api/notations/?limit=15&offset=15",
        "previous": null,
        "results": [
            {
                "pk": 1,
                "employee": "http://localhost:8000/api/employees/1/",
                "widget": "http://localhost:8000/api/widgets/48/",
                "rating": 5
            },

            ...


        ]
    }

==========================
Get an instance of a model
==========================

Example :

.. code-block:: python

    >>> r = requests.get("http://localhost:8000/api/employees/2/")


Gives

.. code-block:: python

    {
        "pk": 2,
        "last_name": "last_name1",
        "first_name": "first_name1",
        "birth_date": "1995-06-15",
        "joined_date": "2012-01-18",
        "salary": 16016.0,
        "phone": "0600000001",
        "performance_indice": 5,
        "gender": "M",
        "children_number": 14,
        "adress": "address1",
        "mail": "user1@gmail.com",
        "married": true
    }


===================
Get recommandations
===================

Get the top ``12`` recommandations for employee with ``pk=28`` :

.. code-block:: python

    >>> r = requests.get("http://localhost:8000/api/employees/28/recommend_widgets/?predictions_number=12")

Gives

.. code-block:: python

    {
        "status": "OK",
        "prediction": [
            [
                "11",
                "17",
                "69",
                "24",
                "4",
                "58",
                "52",
                "30",
                "82",
                "18",
                "7",
                "100"
            ]
        ]
    }

====================
Force model training
====================

Force the model training

.. code-block:: python

    >>> r = requests.get("http://localhost:8000/api/employees/train/")

Gives

.. code-block:: python

    {
        "widgets": 100,
        "notations": 32372,
        "employees": 6040,
        "status": "OK"
    }
