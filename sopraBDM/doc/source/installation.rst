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
    git clone origin https://github.com/goujonpa/sopraBigDataModule.git


======================
Asking for source code
======================

As an alternative, you can also ask me for the full sources by email (available on my github profile)

=================
Project structure
=================

Once downloaded the source, you should get the following project structure:

TO WRITE


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



**************
Database Setup
**************

==========
PostgreSQL
==========


======
Others
======


***********
Supervisord
***********

=====================
What is supervisord ?
=====================

=============
Configuration
=============


********
Starting
********

====================
Start, Stop, Restart
====================














