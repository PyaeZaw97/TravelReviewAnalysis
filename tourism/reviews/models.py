from django.db import models
from .forms import AddReview
from django.urls import reverse

# Create your models here.
class Place(models.Model):
    
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=600)
    image = models.FilePathField(path="/images")

    def __str__(self):          
        return (self.title)


class Review(models.Model):  
	reviewer = models.CharField(max_length=100)
	place_name=models.ForeignKey(Place, on_delete=models.CASCADE)
	image=models.ImageField(upload_to='images/', blank=True)
	review = models.TextField(max_length=10000)
	# pub_date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return (self.reviewer)



	
