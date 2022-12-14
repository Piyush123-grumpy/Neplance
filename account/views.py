
from MySQLdb import ProgrammingError
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect 
from .forms import FreelancerSignUpForm,UserCreationForm,EmployerSignUpForm, freelancer
from django.contrib import auth, messages
from .models import Employer, Freelancer
from gig.models import Gig, Application
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    return render(request,'account/register.html')
def signup_freelancer(request):
    form=FreelancerSignUpForm()
    if request.method == 'POST':
        form=FreelancerSignUpForm(request.POST)
        print(form)
        if form.is_valid():
            print("asdasd")
            f=form.save()
            f.save()
            Freelancer.objects.create(user=f)
            return redirect('/')
    context={"form":form}
    return render (request,"account/signup.html",context)
def signup_employer(request):
    form=EmployerSignUpForm()
    if request.method == 'POST':
        form=EmployerSignUpForm(request.POST)
        print(form)
        if form.is_valid():
            print("asdasd")
            f=form.save()
            f.save()
            Employer.objects.create(user=f)
            return redirect('/')
    context={"form":form}
    return render (request,"account/employer_signup.html",context)

def loginpage(request):
    if request.user.is_authenticated:
        print("okay")
        messages.warning(request,"You are already logged in")
        return redirect('/')

    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            print(name)
            passwd = request.POST.get('password')
            print(passwd)
            user = authenticate(request, username=name, password=passwd)
            
            if user is not None and user.is_freelancer==True:
                login(request, user)
                print("sss")
                messages.success(request,"Logged in Successfully")
                return redirect("/")
            elif user is not None and user.is_employer==True:
                login(request, user)
                print("ass")
                messages.success(request,"Logged in Successfully")
                return redirect("/")
            
            else:
                messages.error(request, "Invalid Username or Password")
                print("Okay")
                return redirect("/login")
        return render(request,"account/login.html")

def reviews(request):
    return render(request,'account/review.html')

@login_required(login_url='/login/')
def appliedJobs(request):
    freelancer=Freelancer.objects.get(user_id=request.user.id)
    applied = Application.objects.filter(Freelancer=freelancer)
    context = {'applied': applied}
    return render(request, 'account/appliedJobs.html', context)

def Logout(request):
    logout(request)
    return redirect('/')

def recievable(request):
    if request.user.is_freelancer:
        applications = Application.objects.filter(Freelancer = Freelancer.objects.get(user=request.user), status="Completed")
        return render(request, 'userdetail/recievable.html', {'applications': applications})
    return redirect('/')


def payable(request):
   
    return redirect('/')
# def addgigs(request):
#     return render(request,'account/addgigs.html')

