from turtle import mode
from django.db import models
from account.models import User
# Create your models here.
class session(models.Model):
    name=models.CharField(verbose_name="Name",max_length=100,blank=True, null=True)

    def __str__(self):
        return self.name

class participants(models.Model):
    session=models.ForeignKey(session,on_delete=models.CASCADE,blank=True, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.user.username

class message(models.Model):
    session=models.ForeignKey(session,on_delete=models.CASCADE,blank=True, null=True)
    user=models.CharField(verbose_name="User",max_length=30,blank=True, null=True)
    message=models.TextField(verbose_name="Message",max_length=10000000,blank=True, null=True)

    def __str__(self):
        return self.user