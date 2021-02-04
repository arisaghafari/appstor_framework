from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)    
    def __str__(self):
        return self.title

class App(models.Model):
    STATUS_CHOICES = (
        ('p', 'pay'),
        ('n', 'without pay')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ManyToManyField(Category, related_name="apps")
    description = models.TextField()
    thumbnail = models.ImageField(upload_to = "images")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    priority = models.IntegerField()
    rateCounter = models.IntegerField()
    Rate = models.FloatField()
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    def __str__(self):
        return self.title

class Comment(models.Model): 
    post = models.ForeignKey(App, on_delete = models.CASCADE, related_name ='comments') 
    user = models.ForeignKey(User, on_delete = models.CASCADE) 
    content = models.TextField() 
    def __str__(self):
        return self.title