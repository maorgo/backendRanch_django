from django.db import models
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=150)
    introduction = RichTextField()
    content = RichTextField()
    slug = models.SlugField(max_length=150, default='')
    tags = TaggableManager()
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
