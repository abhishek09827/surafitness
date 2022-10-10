from hashlib import blake2b
from lib2to3.pgen2 import token
from turtle import title
from django.db import models
from froala_editor.fields import FroalaField
from .helper import *
#  It contains the essential fields and behaviors of the data you’re storing 
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)


class BlogModel(models.Model):
    title = models.CharField(max_length = 1000)
    content = FroalaField()
# A Slug is basically a short label for something, containing only letters, numbers, underscores or hyphens
    user = models.ForeignKey(User, blank=True, null=True, on_delete = models.CASCADE)
    slug = models.SlugField(max_length = 1000, null=True, blank=True)
    image = models.ImageField(upload_to = 'blog')
#auto_now_add=True will not change if we change it later
    created_at = models.DateTimeField(auto_now_add=True)
#auto_now = True called every time this model will be updated
    upload_to = models.DateTimeField(auto_now = True)
# pillow library is used to handle images in python  
# Create your models here.
    def __str__(self):
        return self.title
#*args (Non-Keyword Arguments)
#**kwargs (Keyword Arguments)
    def save(self, *args, **kwargs):
            self.slug = generate_slug(self.title)
            super(BlogModel,self).save(*args, **kwargs)
