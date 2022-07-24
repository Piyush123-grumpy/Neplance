from django import forms
from .models import Gig

class AddGigForm (forms.ModelForm):
    class Meta:
        model = Gig
        fields = ['title', 'company', 'image', 'description', 'country', 'city', 'area', 'pay', 'contact', 'category']
        # Custom attributes to ModelForm fields.
        widgets= {
            'description':forms.Textarea(attrs={'class': 'x', 'placeholder': 'Job Description'}),
            'country':forms.Select(attrs={'class': 'country-input', 'placeholder': 'Job Description'}),
            'category':forms.Select(attrs={'class': 'country-input', 'placeholder': 'Job Description'}),
        }