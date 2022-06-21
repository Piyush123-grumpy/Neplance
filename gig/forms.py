from django import forms
from .models import Gig

class AddGigForm (forms.ModelForm):
    class Meta:
        model = Gig
        fields = ['title', 'description', 'pay', 'category']
        # Custom attributes to ModelForm fields.
        widgets= {
            'description':forms.Textarea(attrs={'class': 'x', 'placeholder': 'Job Description'}),
        }