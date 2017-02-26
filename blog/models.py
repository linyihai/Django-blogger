from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Article(models.Model):
    # see data field
    # https://docs.djangoproject.com/en/1.15/ref/models/fields/
    title = models.CharField(max_length=32, default="Title")
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.title
