from django.db import models


class User(models.Model):
    username = models.CharField(max_length=128)


class Topic(models.Model):
    name = models.CharField(max_length=128)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topics = models.ManyToManyField(Topic, blank=True)

    class Meta:
        ordering = ['-created']