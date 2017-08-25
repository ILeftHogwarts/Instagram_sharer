from django.db import models

# Create your models here.
class InstaPost(models.Model):
    user_name = models.CharField(max_length = 50)
    media_file = models.FileField()
    tag = models.CharField(max_length = 50)
    description = models.TextField()

class User(models.Model):
    name = models.CharField(max_length = 50)
    sername = models.CharField(max_length = 50)
    access_token = models.CharField(max_length = 100)
    user_post = models.ForeignKey(InstaPost, on_delete=models.CASCADE)