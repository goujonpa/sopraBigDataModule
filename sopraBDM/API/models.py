from __future__ import unicode_literals


from django.db import models

# Create your models here.

class Employee(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    joined_date = models.DateField()
    salary = models.FloatField()
    phone = models.CharField(max_length=50)
    performance_indice = models.IntegerField()
    gender = models.CharField(max_length=1)
    children_number = models.IntegerField()
    adress = models.TextField()
    mail = models.EmailField()
    married = models.BooleanField()

class Widget(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()

class Notation(models.Model):
    employee = models.ForeignKey('Employee')
    widget = models.ForeignKey('Widget')
    rating = models.IntegerField()

