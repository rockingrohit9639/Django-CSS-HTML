from django.db import models
from django.urls import reverse

# Create your models here.
class Challenges(models.Model):
	title		= models.TextField()
	content 	= models.TextField()
	active		= models.TextField()

def get_absolute_url(self):
		return reverse("challenges:challenges-detail", kwargs={"id": self.id})
# Create your models here.
#def get_absolute_url(self):
		#return reverse("products:product-detail", kwargs={"id": self.id})