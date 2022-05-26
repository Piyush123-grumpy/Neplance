
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect 
from .forms import FreelancerSignUpForm,UserCreationForm,EmployerSignUpForm
from django.contrib import auth, messages

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
            form.save()
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
            form.save()
            return redirect('/')
    context={"form":form}
    return render (request,"account/employer_signup.html",context)

def loginpage(request):
    if request.user.is_authenticated:
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
                return redirect("dashboard/")
            elif user is not None and user.is_employer==True:
                login(request, user)
                print("ass")
                messages.success(request,"Logged in Successfully")
                return redirect("dashboard/")
            
            else:
                messages.error(request, "Invalid Username or Password")
                print("Okay")
                return redirect("/login")
        return render(request,"account/login.html")


