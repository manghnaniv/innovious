from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Product(models.Model):
	
#	def __str__(self):
#		return self.name
	
	name = models.CharField(max_length = 100)
	short_detail = models.CharField(max_length = 500)
	long_detail =models.TextField(blank = True)
	product_image = models.FileField()
	datetime = models.DateTimeField(auto_now = True)
	
