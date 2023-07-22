from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    uploaded_by = models.ForeignKey(User,on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    video_file = models.FileField(upload_to='videos/')


