from unittest.util import _MAX_LENGTH
from django.db import models
from Neplance.account.models import Employer,Freelancer
from account import models
# Create your models here.
class ReviewRating(models.Model):
    employer=models.Foreignkey(Employer,on_delete=models.CASCADE)
    freelancer=models.Foreignkey(Freelancer,on_delete=models.CASCADE)
    review=models.TextField(m)