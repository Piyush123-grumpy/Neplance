from asyncio.windows_events import NULL
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations=True

    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError('Email is require')
        email = self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True) 
        extra_fields.setdefault('is_superuser',True) 
        extra_fields.setdefault('is_active',True) 
        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Super user must have is_staff'))
        return self.create_user(email,password,**extra_fields)

class User(AbstractUser):
    is_freelancer=models.BooleanField(default=False)
    is_employer=models.BooleanField(default=False)

   

class Freelancer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    language=models.CharField(verbose_name="Language",max_length=30,blank=True, null=True)
    education=models.CharField(verbose_name="Education",max_length=30,blank=True, null=True)
    current_job=models.CharField(verbose_name="Current Job",max_length=100,blank=True, null=True)
    city=models.CharField(verbose_name="City",max_length=100,blank=True, null=True)
    country=models.CharField(verbose_name="Country",max_length=100,blank=True, null=True)
    profile_picture=models.ImageField(upload_to='',default='',blank=True, null=True)
    

    def __str__(self):
        return self.user.username

class portfolio(models.Model): 
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE, primary_key=True)
    Project_title=models.CharField(verbose_name="Porject Title",max_length=100,blank=True, null=True)


class Other_experience(models.Model): 
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE, primary_key=True)
    SUbject=models.CharField(verbose_name="Subject",max_length=100,blank=True, null=True)
    description=models.CharField(verbose_name="Description",max_length=100,blank=True, null=True)
    



class employment_history(models.Model):
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE, primary_key=True)
    company=models.CharField(verbose_name="Company",max_length=100,blank=True, null=True)
    city=models.CharField(verbose_name="City",max_length=100,blank=True, null=True)
    Title=models.CharField(verbose_name="Title",max_length=100,blank=True, null=True)
    period=models.CharField(verbose_name="Period",max_length=100,blank=True, null=True) 
    description=models.CharField(verbose_name="Description",max_length=100,blank=True, null=True)



class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
