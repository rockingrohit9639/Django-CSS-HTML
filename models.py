from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
	title		= models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	price		= models.DecimalField(decimal_places=2, max_digits=10)
	summary		= models.TextField()
	date		= models.DateField(null=True)
	contact		= models.EmailField(max_length=254)
	featured	= models.NullBooleanField()
	
	def get_absolute_url(self):
		return reverse("products:product-detail", kwargs={"id": self.id})