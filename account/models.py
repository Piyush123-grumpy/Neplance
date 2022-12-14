from distutils.command.upload import upload
from email.policy import default
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from phonenumbers import PhoneNumberDesc


# Create your models here.

class User(AbstractUser):
    is_freelancer=models.BooleanField(default=False)
    is_employer=models.BooleanField(default=False)
    def getFreelancer(self):
        return self.freelancer_set.get(user=self)

class Freelancer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language=models.CharField(verbose_name="Language",max_length=30,blank=True, null=True)
    education=models.CharField(verbose_name="Education",max_length=30,blank=True, null=True)
    current_job=models.CharField(verbose_name="Current Job",max_length=100,blank=True, null=True)
    city=models.CharField(verbose_name="City",max_length=100,blank=True, null=True)
    country=models.CharField(verbose_name="Country",max_length=100,blank=True, null=True)
    profile_picture=models.ImageField(upload_to='',default='default.jpg',blank=True, null=True)
    description=models.CharField(verbose_name="Description",max_length=300,blank=True, null=True)

    def __str__(self):
        return self.user.username
class portfolio(models.Model): 
    freelancer=models.ForeignKey(Freelancer,on_delete=models.CASCADE,blank=True, null=True)
    Project_title=models.CharField(verbose_name="Porject Title",max_length=100,blank=True, null=True)
    description=models.CharField(verbose_name="Description",max_length=300,blank=True, null=True)
    date=models.DateField(blank=True, null=True)

    def __str__(self):
        return self.Project_title



class Other_experience(models.Model): 
    freelancer=models.ForeignKey(Freelancer,on_delete=models.CASCADE,blank=True, null=True)
    SUbject=models.CharField(verbose_name="Subject",max_length=100,blank=True, null=True)
    description=models.CharField(verbose_name="Description",max_length=300,blank=True, null=True)
    



class employment_history(models.Model):
    freelancer=models.ForeignKey(Freelancer,on_delete=models.CASCADE,blank=True, null=True)
    company=models.CharField(verbose_name="Company",max_length=100,blank=True, null=True)
    city=models.CharField(verbose_name="City",max_length=100,blank=True, null=True)
    Title=models.CharField(verbose_name="Title",max_length=100,blank=True, null=True)
    period=models.DateField(blank=True, null=True)
    description=models.CharField(verbose_name="Description",max_length=300,blank=True, null=True)

    def __str__(self):
        return self.company




class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name=models.CharField(verbose_name="First Name",max_length=30,blank=True, null=True)
    last_name=models.CharField(verbose_name="Last Name",max_length=30,blank=True, null=True)
    email=models.EmailField(verbose_name="Email",max_length=30,blank=True, null=True)
    country = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    PhoneNumber= PhoneNumberField(blank=True)
    profile_picture=models.ImageField(upload_to='',default='',blank=True, null=True)
    description=models.CharField(verbose_name="Description",max_length=300,blank=True, null=True)

    def __str__(self):
        return self.user.username
