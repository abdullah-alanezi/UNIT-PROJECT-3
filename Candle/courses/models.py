from django.db import models
from django.contrib.auth.models import User
from experts.models import ExpertProfile
# Create your models here.

class Course(models.Model):
    expert_profile = models.ManyToManyField(ExpertProfile)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/',default="images/default.jpg")


class CourseContent(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    video_title =models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/',default='videos/default.mp4')