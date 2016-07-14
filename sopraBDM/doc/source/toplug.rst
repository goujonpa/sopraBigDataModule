################
How to plug in ?
################

There are several ways to use our code within your app. Here we describe the steps to integrate it.

==================
Installing the app
==================

Obviously. Read the intallation section to achieve it.

============================
Integration to your database
============================

The first step after installing the app would be to link our app to your database so that we access the informations you have on your users (particularly their notations of the widgets). Therefore, you could have to modify the code in the ``./API/models.py`` file in order to make the models fit your DB.

===========
HTTP server
===========

The second step would be to setup a real HTTP server instead of the Django development server. As previously said, `NginX`_ is a really good candidate and there are good documentations online to integrate it with Django.

.. _NginX: https://www.nginx.com/resources/wiki/

=============
Configuration
=============

Finally, you might have to change some of the projects settings to fit your server.


======================================
Alternative : using the R scripts only
======================================

The most valuable part of our application are the R scripts. If you don't succeed in installing the application, you still have the option to re-use the R scripts only, and adapt them a bit to fit your needs.

