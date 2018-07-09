from django.db import models
from django.utils.safestring import mark_safe
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=150)
    introduction = mark_safe(models.TextField(max_length=500))
    content = mark_safe(models.TextField(max_length=99999))
    slug = models.SlugField(max_length=150, default='')
    tags = TaggableManager()
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
