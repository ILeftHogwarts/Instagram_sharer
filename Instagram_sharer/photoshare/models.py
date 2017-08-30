from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 50)
    user_id = models.CharField(max_length = 50)
    access_token = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
        


class PostTags(models.Model):
    tag = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.tag

class InstaPost(models.Model):
    type_choices = [
        ('videos', 'video'),
        ('images', 'image')
    ]
    user_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, default = None)
    url = models.CharField(max_length = 100, default = 'default')
    type = models.CharField(max_length = 6, choices = type_choices, default = 'image')
    tag = models.ManyToManyField(PostTags)
