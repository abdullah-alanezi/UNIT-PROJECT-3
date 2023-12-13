from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subcriptions = models.ManyToManyField(User, related_name="subscriptions")
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/',default="images/default.jpg")
    description = models.TextField()
    addition_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class CourseContent(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    video_title =models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/',default='videos/default.mp4')

    def __str__(self) -> str:
        return self.video_title