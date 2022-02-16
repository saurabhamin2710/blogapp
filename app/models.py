from turtle import title
from django.db import models

# Create your models here.


class Cards(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
