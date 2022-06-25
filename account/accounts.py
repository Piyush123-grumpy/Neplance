from re import I
from django.http import HttpResponse
from django.shortcuts import render,redirect

from account.forms import employer, freelancer,Portofolio,employmentHistory,otherExperience
from .models import Employer, Freelancer,portfolio,employment_history,Other_experience

from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def account_detail(request):
    if request.user.is_freelancer:
        user=request.user
        freelancer=Freelancer.objects.filter(user=user)[0]
        Portfolio=portfolio.objects.filter(freelancer=freelancer)
        Employment=employment_history.objects.filter(freelancer=freelancer)
        other_exp=Other_experience.objects.filter(freelancer=freelancer)
        context={
            'user':user,
            'freelancer':freelancer,
            'portoflio':Portfolio,
            'Employment':Employment,
            'other_exp':other_exp}
        return render(request,'account/account_detail.html',context)
    else:
        employer=Employer.objects.get(user=request.user)
        return render(request,'account/employer_detail.html',{"employer":employer})
def editUser(request):
    return render(request, 'userdetail/profile.html')

def editemployer(request):
    return render(request, 'userdetail/employer_edit.html')

def Freelancer_info_save(request):
    user=request.user
    object=Freelancer.objects.get(user_id=user)
    
    if request.method == "POST" or request.method == "FILES":
        form=freelancer(request.POST,request.FILES,instance=object)
        form.save()
    

    return redirect("account_detail")


def Employer_info_save(request):
    user=request.user
    object=Employer.objects.get(user_id=user)
    
    if request.method == "POST" or request.method == "FILES":
        form=employer(request.POST,request.FILES,instance=object)
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

def delete_employment(request,pk):
    employment_his=employment_history.objects.get(id=pk)
    employment_his.delete()
    return redirect("account_detail")
    
def delete_portofolio(request,pk):
    portofolio=portfolio.objects.get(id=pk)
    portofolio.delete()
    return redirect('account_detail')

def delete_other_exp(request,pk):
    other_exp=Other_experience.objects.get(id=pk)
    other_exp.delete()
    return redirect('account_detail')

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

