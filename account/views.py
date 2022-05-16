
from django.http import HttpResponse
from django.shortcuts import render,redirect 
from .forms import FreelancerSignUpForm,UserCreationForm,EmployerSignUpForm

# Create your views here.
def home(request):
    return render(request,'account/basic.html')
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