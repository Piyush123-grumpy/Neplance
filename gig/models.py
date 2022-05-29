from ast import Str
from unicodedata import category
from unittest.util import strclass
from django.db import models
from account.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name


class Gig (models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=255, null=True)
    pay = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, unique=True)
    
    def __str__(self):
        return self.title