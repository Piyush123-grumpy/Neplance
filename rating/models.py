
from django.db import models
from account.models import Employer,Freelancer

# Create your models here.
class ReviewRating(models.Model):
    employer=models.ForeignKey(Employer,on_delete=models.CASCADE)
    freelancer=models.ForeignKey(Freelancer,on_delete=models.CASCADE)
    review=models.TextField(max_length=500,blank=True)
    rating=models.FloatField()

