from wsgiref.validate import validator
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.forms import ModelForm

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
    
