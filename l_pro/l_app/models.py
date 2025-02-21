from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class restaurant(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    rating = models.IntegerField(default=0)
    discription = models.TextField(max_length=500)
    feedimage = models.ImageField(upload_to='restaurant_images/')
   
