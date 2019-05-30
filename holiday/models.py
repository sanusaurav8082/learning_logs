# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
From datetime import date

# Create your models here.
class Reporter(models.Model):
	"""creating a new model in the given web application"""
	name=models.textField()
	

	def __str__(self):
		"""Returns a string representation of the model"""
		return self.name
class Article(models.Model):
	"""creating a new article model"""
	heading=models.CharField(max_length=200)
	content=models.textField()
	date=date.today()
	reporter=models.ForeignKey(Reporter)
	
	def __str__(self):
		"""return a string representation of the model"""
		return self.heading
