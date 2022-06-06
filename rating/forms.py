from dataclasses import fields
from rating.models import ReviewRating
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model=ReviewRating
        fields=["review","rating"]