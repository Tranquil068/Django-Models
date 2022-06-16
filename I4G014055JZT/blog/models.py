from django.db import models
from pkg_resources import get_supported_platform
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    Title=models.CharField(max_length=200)
    Text=models.TextField(max_length=1000)
    Author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    Created_date=models.DateTimeField
    Published_date=models.DateTimeField