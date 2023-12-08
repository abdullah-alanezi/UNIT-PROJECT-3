from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ExpertProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(upload_to="images/",default="images/default.jpg")
    
    


class ExpertExperience(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    experience = models.CharField(max_length=255)
    experience_years =models.IntegerField()
