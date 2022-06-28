import re
from webbrowser import get
from django.shortcuts import redirect, render
from django.db import IntegrityError
from django.db.models import Sum
from account.forms import freelancer
from rating.forms import ReviewForm
from .models import Employer, Freelancer,ReviewRating
# Create your views here.
def review(request):
    return render(request,'review.html')
def rating(request):
    freelancer=Freelancer.objects.get(user_id=2)
    sum=ReviewRating.objects.filter(freelancer_id=2).aggregate(Sum('rating'))
    number=ReviewRating.objects.filter(freelancer_id=2).count()   
    avg_rating=sum["rating__sum"]/number
    context={"freelancer":freelancer,"avg_rating":avg_rating}
    return render(request,'rate.html',context)

def submit_review(request,freelancer_id):
    print(freelancer_id)
    url=request.META.get('HTTP_REFERER')
    freelance=Freelancer.objects.get(user_id=freelancer_id)
    employid=Employer.objects.get(user_id=request.user)
    print(employid)
    try:
        review= ReviewRating.objects.get(employer=employid,freelancer=freelance)
        form=ReviewForm(request.POST,instance=review)
        form.save()
        return redirect(url)     
    except ReviewRating.DoesNotExist:
        form=ReviewForm(request.POST)
        if form.is_valid():
            data=ReviewRating()
            data.rating=form.cleaned_data["rating"]
            data.review=form.cleaned_data["review"]
            data.employer=employid
            data.freelancer=freelance
            data.save()
            return redirect(url)


    