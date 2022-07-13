from django.db import models


# Create your models here.
class Feed(models.Model):
    user_id = models.TextField()
    content = models.TextField()
    image = models.TextField()
    profile_image = models.TextField()
    like_count = models.IntegerField()
