from django.db import models
from django.contrib.auth.models import User
from courses.models import Course
# Create your models here.

class ExpertProfile(models.Model):
    experience_fields =models.TextChoices("experience_fields",['Programming',"Law","Sciences"])
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(upload_to="images/",default="images/default.jpg")
    experience_field =models.CharField(max_length=56,choices = experience_fields.choices, default="Sciences")

    def __str__(self) -> str:
        return self.user.first_name
    

    


class ExpertExperience(models.Model):
    
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    experience = models.CharField(max_length=255)
    experience_years =models.IntegerField()
    

    def __str__(self) -> str:
        return self.experience
