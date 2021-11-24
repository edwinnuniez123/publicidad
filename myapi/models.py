#from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=80)
    logo = models.URLField(max_length=300)

class Store(models.Model):
	brand =  models.ForeignKey('Brand', on_delete=models.CASCADE,)
	identifier = models.CharField(max_length=80)
	name = models.CharField(max_length=80)
	address = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Deal(models.Model):
	name = models.CharField(max_length=80)
	store = models.ForeignKey('Store', on_delete=models.CASCADE,)
	image = models.URLField(max_length=300)   
	price = models.DecimalField(max_digits=6, decimal_places=3)

	def __str__(self):
		return self.name