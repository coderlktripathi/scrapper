from django.db import models

class Product(models.Model):
    
	name = models.CharField(max_length=256, null=True)
	price = models.CharField(max_length=100, null=True)
	description = models.TextField(null=True)
	sku = models.CharField(max_length=100, null=True)
	web_url = models.CharField(max_length=1000)

	def __str__(self):
		return self.name
