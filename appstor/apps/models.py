from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import random


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Property(models.Model):
    title = models.CharField(max_length=200)
    value = models.CharField(max_length=400)
    def __str__(self):
        return self.title + " : " + self.value

class App(models.Model):
    title=models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ManyToManyField(Category, related_name="apps")
    pr = models.ManyToManyField(Property, related_name="apps")
    thumbnail = models.ImageField(upload_to="images")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description=models.TextField()
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(App, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    #def __str__(self):
    #    return self.user.username
