from re import I
from django.http import HttpResponse
from django.shortcuts import render,redirect

from account.forms import freelancer,Portofolio,employmentHistory,otherExperience
from .models import Employer, Freelancer

def account_detail(request):
    return render(request,'account/account_detail.html')

def editUser(request):
    return render(request, 'userdetail/profile.html')

def Freelancer_info_save(request):
    user=request.user
    object=Freelancer.objects.get(user_id=user)
    
    if request.method == "POST" or request.method == "FILES":
        form=freelancer(request.POST,request.FILES,instance=object)
        form.save()
    

    return redirect("account_detail")
def Portoflio(request):
    user=request.user
    return render(request, 'userdetail/portfolio.html',{"user":user})

def save_protfolio(request):
    if request.method == "POST":
        form=Portofolio(request.POST)
        form.save()
    return redirect("account_detail")



def Employment_history(request):
    user=request.user
    return render(request, 'userdetail/employment_history.html',{"user":user})

def save_employment_history(request):
    if request.method == "POST":
        form=employmentHistory(request.POST)
        form.save()
    return redirect("account_detail")

def other_experience(request):
    user=request.user
    return render(request, 'userdetail/other_experiences.html',{"user":user})
def save_other_experience(request):
    if request.method == "POST":
        form=otherExperience(request.POST)
        form.save()
    return redirect("account_detail")

