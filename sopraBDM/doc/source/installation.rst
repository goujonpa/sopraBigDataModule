##################
Installation Guide
##################

**********************
Dowloading the project
**********************

The project is available on Github or you can ask me for the source code.

===========
Github Fork
===========

First, fork the project on `github`_.

.. _github: https://github.com/goujonpa/sopraBigDataModule

Then, clone it into your project directory (change the username in URL):

.. code-block:: bash

    mkdir project
    git clone https://github.com/goujonpa/sopraBigDataModule.git


======================
Asking for source code
======================

As an alternative, you can also ask me for the full sources by email (available on my github profile)

=================
Project structure
=================

Once downloaded the source, you should get the following project structure:

.. code-block:: python

    ./  # Project root

        /API            # contains all of the API logic
        /RLib           # contains the R script and the json exchange files
        /doc            # contains the sources of this doc
        /sopraBDM       # contains the settings files of the project
        /supervisord    # contains the configuration files of the supervisord


***********************
Python and dependencies
***********************

The next thing to do is to setup your python environment.

==============
Python version
==============

The version we used to develop the project is python 2.7.11. Make sure your python version is the same if you want the project to work.

================
Pip & Virtualenv
================

Python should be supplied with a working version of `pypi`_.

.. _pypi: https://pypi.python.org/pypi

What you now want to do is to set up a virtual python environment, in order to avoid messing up your other python projects. This can by accomplished thanks to the python module "virtualenv" :

.. code-block:: bash

    pip install virtualenv
    virtualenv venv

That you then activate by using the command :

.. code-block:: bash

    source venv/bin/activate

And deactivate by using :

.. code-block:: bash

    deactivate

.. warning::

    MAKE SURE YOUR VIRTUAL ENV IS ALWAYS ACTIVATED WHEN YOU WORK ON THE PROJECT


=============================
Dependencies and requirements
=============================

Now you have set up a virtual environment, you can install every python dependency by using

.. code-block:: bash

    pip install -r requirements.txt

**************
Database Setup
**************

==========
PostgreSQL
==========

We used a PostgreSQL database to develop our solution. The database settings are located in :

``./sopraBDM/settings.py``

You should update them to be able to connect to your database :

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'sopraDB',
            'HOST': '127.0.0.1',
            'PORT': '5432',
            'USER': 'sopra',
            'PASSWORD': 'tx',
        }
    }


======
Others
======

Otherwise, you can adapt the code fairly easily following `django's documentation`_.

.. _django's documentation: https://docs.djangoproject.com/en/1.9/ref/databases/

=======
Migrate
=======

To finish your database setup, you have to initialise its structure thanks to the django ORM by using :

.. code-block:: bash

    python manage.py makemigrations
    python manage.py Migrate

This should initialise your DB structure


***********
Supervisord
***********

=====================
What is supervisord ?
=====================

Supervisord (`click here to access supervisord's documentation`_) is a process manager. We use it to launch every process used by our project in just a few commands.

.. _click here to access supervisord's documentation: http://supervisord.org/index.html


********
Starting
********

====================
Start, Stop, Restart
====================

You should now be able to start the app by using :

.. code-block:: bash

    supervisord -c supervisord.conf

and control it by connecting to the supervisord controller :

.. code-block:: bash

    supervisorctl -c supervisord.conf
    start all
    restart all
    stop all
    ...


