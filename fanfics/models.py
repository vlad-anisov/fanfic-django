from django.db import models
from taggit.managers import TaggableManager
from django.conf import settings


class Fanfic(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField()
    genre = models.CharField(max_length=50)
    tags = TaggableManager()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    fanfic = models.ForeignKey(Fanfic, on_delete=models.CASCADE )