################
Technology Stack
################

Here is a quick sum up of the used technologies for that project (and links for their documentations)

================
Python framework
================

`Django`_.

.. _Django: https://docs.djangoproject.com/en/1.9/


===========
HTTP Server
===========

In the context of our development, we have used the integrated Django development server (using ``python manage.py runserver``).

In a production environment, you shouldn't use the Django development server as its performance are not good enough. We advice you to set up an HTTP server ready to be used in that context such as `NginX`_.

.. _NginX: https://www.nginx.com/resources/wiki/

==============
REST framework
==============

We used `Django REST Framework`_ to develop easily our browsable API.

.. _Django REST Framework: http://www.django-rest-framework.org/


==================
Asynchronous tasks
==================

For any asynchronous task (such as the task handling the train of our prediction model, every night), we use python's module `Celery`_.

.. _Celery: http://docs.celeryproject.org/en/latest/index.html

==============================
Data Mining & Machine Learning
==============================

We use the `R`_ language for all of the Data Mining and Machine Learning parts of our solution.

.. _R: http://www.tutorialspoint.com/r/

===========
Supervisord
===========

The handling of all of the daemon process is operated by `Supervisord`_.

.. _Supervisord: http://supervisord.org/

=============
Documentation
=============

We use `Sphinx`_ to write our documentation.

.. _Sphinx: http://www.sphinx-doc.org/en/stable/index.html


