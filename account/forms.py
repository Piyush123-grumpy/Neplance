import email
from pyexpat import model
from statistics import mode
from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import User
from django.db import transaction,models
from .models import Employer, Freelancer,portfolio,employment_history,Other_experience

class FreelancerSignUpForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'but','placeholder':'Username'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'but','placeholder':'Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'but','placeholder':'Enter password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'but','placeholder':'Confirm password'}))
    class Meta(UserCreationForm.Meta):
        model= User
    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.is_freelancer=True
        user.save()
        return user 

class EmployerSignUpForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'but','placeholder':'Username'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'but','placeholder':'Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'but','placeholder':'Enter password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'but','placeholder':'Confirm password'}))
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_employer=True
        if commit:
            user.save()
        return user

class freelancer(forms.ModelForm):
    class Meta:
        model=Freelancer
        fields=['language','education','current_job','city','country','description','profile_picture']

class employer(forms.ModelForm):
    class Meta:
        model=Employer
        fields=['first_name','last_name','PhoneNumber','city','country','description','profile_picture','email']

class Portofolio(forms.ModelForm):
    class Meta:
        model=portfolio
        fields=["Project_title","description","date"]
class employmentHistory(forms.ModelForm):
    class Meta:
        model=employment_history
        fields=["company","city","Title","period","description"]
class otherExperience(forms.ModelForm):
    class Meta:
        model=Other_experience
        fields=["SUbject","description"]
