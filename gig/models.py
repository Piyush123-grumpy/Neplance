from unicodedata import category
from django.db import models
from account.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)

class Gig (models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=255, null=True)
    pay = models.IntegerField(null=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, unique=True)
    