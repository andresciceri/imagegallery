from django.db import models

# Create your models here.

class ImageGallery(models.Model):
	image_url 	= models.URLField(max_length=500)
	image_name	= models.CharField(max_length=200)

	def __str__(self):
		return self.image_name