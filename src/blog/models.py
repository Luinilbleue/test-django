from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):

    # Fields
    # each field match a key in the DB
    title = models.CharField(max_length=64)
    ctime = models.DateTimeField(default=timezone.now)
    short_description = models.TextField(max_length=256)
    content = models.TextField()
    image = models.URLField()
    slug = models.SlugField()


    def __str__(self):
        return self.title



class Comment(models.Model):

    # Fields
    # each field match a key in the DB
    ctime = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=256)
    linked_post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )


    def __str__(self):
        return 'Comment on {0} at {1}'.format(self.linked_post, self.ctime)