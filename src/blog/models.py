from django.db import models
from django.utils import timezone

class Post(models.Model):

    # Fields
    title = models.CharField(max_length=64)
    ctime = models.DateTimeField(default=timezone.now)
    short_description = models.TextField(max_length=256)
    content = models.TextField()
    image = models.URLField()
    slug = models.SlugField(unique_for_date=True)

