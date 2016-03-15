from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Funeral(models.Model):
    name = models.CharField(max_length=250)
    body = models.TextField()
    house_position = models.CharField(max_length=200, null=True, blank=True)
    mosque_position = models.CharField(max_length=200, null=True, blank=True)
    place_tags = TaggableManager()
    author = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        db_table = 'funeral'
        ordering = ['-create_date']

    def __str__(self):
        return self.name
