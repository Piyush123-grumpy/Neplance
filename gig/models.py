from ast import Str
from unicodedata import category
from unittest.util import strclass
from django.db import models
from account.models import User
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name

class Gig (models.Model):
    title = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to ='gigs/', null=False, default="gigs/default.png")
    description = models.CharField(max_length=255, null=True)
    country = country = CountryField(null=False, blank_label='(select country)')
    city = models.CharField(max_length=50, null=False)
    area = models.CharField(max_length=50, null=False) # Locality area name
    pay = models.IntegerField(null=True)
    # contact = PhoneNumberField(default=None)
    contact = PhoneNumberField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def getApplicationCount(self):
        count = self.application_set.all().count()
        return count
    
    def getRequiremets(self):
        requirements = self.requirement_set.filter(gig=self)
        return requirements
    
    def getApplications(self):
        applications = self.application_set.all()
        return applications

    def __str__(self):
        return self.title

class Requirement(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE)
    requirement = models.CharField(max_length=255, null=False)
    def __str__(self):
        return self.gig.title

class Application (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=255, null=True)
    applied_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.gig.title