from re import I
from django.http import HttpResponse
from django.shortcuts import render,redirect

from account.forms import employer, freelancer,Portofolio,employmentHistory,otherExperience
from .models import Employer, Freelancer,portfolio,employment_history,Other_experience
from django.core.exceptions import ObjectDoesNotExist
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
    if request.user.is_freelancer:
        return render(request, 'userdetail/profile.html')
    else:
        return redirect('/')


def Freelancer_info_save(request):
    if request.user.is_freelancer:
        user=request.user
        object=Freelancer.objects.get(user_id=user)
        
        if request.method == "POST" or request.method == "FILES":
            form=freelancer(request.POST,request.FILES,instance=object)
            print(request.POST)
            print(request.FILES)
            form.save()
        

        return redirect("account_detail")
    else:
        return redirect('/')


def editemployer(request):
    if request.user.is_employer:
        return render(request, 'userdetail/employer_edit.html')
    else:
        return redirect('/')

def Employer_info_save(request):
    if request.user.is_employer:
        user=request.user
        object=Employer.objects.get(user_id=user)
        
        if request.method == "POST" or request.method == "FILES":
            form=employer(request.POST,request.FILES,instance=object)
            print(form)
            print(request.POST)
            print(request.FILES)
            form.save()


        return redirect("account_detail")
    else:
        return redirect('/')


#CRUD OF PORTOFOLIO
def Portoflio(request):
    if request.user.is_freelancer:
        return render(request, 'userdetail/portfolio.html',{"user":freelancer})
    else:
        return redirect('/')

def save_protfolio(request):
    if request.user.is_freelancer:
        user=request.user
        freelancer=Freelancer.objects.get(user_id=user)
        if request.method == "POST":
            form=Portofolio(request.POST)
       
            if form.is_valid():
                data=portfolio()
                data.freelancer=freelancer
                data.Project_title=form.cleaned_data["Project_title"]
                data.date=form.cleaned_data["date"]
                data.description=form.cleaned_data["description"]
                data.save()
        return redirect("account_detail")
    else:
        return redirect('/')
def delete_portofolio(request,pk):
    if request.user.is_freelancer:
        try:
            user=request.user
            freelancer=Freelancer.objects.get(user_id=user)
            portofolio=portfolio.objects.get(id=pk,freelancer=freelancer)
            portofolio.delete()
            return redirect('account_detail')
        except ObjectDoesNotExist:
            return redirect('/')

    else:
        return redirect('/')

#CRUD OF EMPLOYMENT HISTORIES
def Employment_history(request):
    if request.user.is_freelancer:
        
        return render(request, 'userdetail/employment_history.html',{"user":freelancer})
    else:
        return redirect('/')

def save_employment_history(request):
    
    if request.user.is_freelancer:
        user=request.user
        freelancer=Freelancer.objects.get(user_id=user)
        if request.method == "POST":
            form=employmentHistory(request.POST)
            if form.is_valid():
                data=employment_history()
                data.freelancer=freelancer
                data.company=form.cleaned_data["company"]
                data.city=form.cleaned_data["city"]
                data.Title=form.cleaned_data["Title"]
                data.period=form.cleaned_data["period"]
                data.description=form.cleaned_data["description"]
                data.save()

        return redirect("account_detail")
    else:
        return redirect('/')

def delete_employment(request,pk):
    if request.user.is_freelancer:
        try:
            user=request.user
            freelancer=Freelancer.objects.get(user_id=user)
            employment_his=employment_history.objects.get(id=pk,freelancer=freelancer)
            employment_his.delete()
            return redirect("account_detail")
        except ObjectDoesNotExist:
            return redirect('/')
    else:
        return redirect('/')
    

#CRud of other experience
def other_experience(request):
    if request.user.is_freelancer:
        
        return render(request, 'userdetail/other_experiences.html',{"user":freelancer})
    else:
        return redirect('/')
def save_other_experience(request):
    if request.user.is_freelancer:
        user=request.user
        freelancer=Freelancer.objects.get(user_id=user)
        if request.method == "POST":
            form=otherExperience(request.POST)
            if form.is_valid():
                data=Other_experience()
                data.freelancer=freelancer
                data.SUbject=form.cleaned_data["SUbject"]
                data.description=form.cleaned_data["description"]
                data.save()
        return redirect("account_detail")
    else:
        return redirect('/')


def delete_other_exp(request,pk):
    if request.user.is_freelancer:
        try:
            user=request.user
            freelancer=Freelancer.objects.get(user_id=user)
            other_exp=Other_experience.objects.get(id=pk,freelancer=freelancer)
            other_exp.delete()
            return redirect('account_detail')
        except ObjectDoesNotExist:
            return redirect('/')
    else:
        return redirect('/')





