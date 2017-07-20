from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Username(models.Model):
    username = models.CharField(max_length=8)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Laptop(models.Model):
    laptopname = models.CharField(max_length=8)

    def __str__(self):
        return self.laptopname

class Dateout(models.Model):
	dateoutbutton = models.CharField(max_length=1)
	dateout = models.DateField(auto_now_add = True)
		
	def __str__(self):
		return self.dateout

class Datein(models.Model):
	dateinbutton = models.CharField(max_length=1)
	datein = models.DateField(auto_now_add = True)

	def __str__(self):
		return self.dateinbutton