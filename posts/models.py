from django.db import models
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=150)
    introduction = models.TextField(max_length=300)
    content = models.TextField(max_length=99999)
    slug = models.SlugField(max_length=150, default='')
    tags = TaggableManager()
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
