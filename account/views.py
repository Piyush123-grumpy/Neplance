
from django.http import HttpResponse
from django.shortcuts import render
from .forms import SignUpForm,UserCreationForm

# Create your views here.
def home(request):
    return render(request,'account/basic.html')
def register(request):
    return render(request,'account/register.html')
def signup(request):
    form=SignUpForm(request.POST)
    if form.is_valid:
        pass
    else:
        form=SignUpForm()
    context={"form":form}
    return render (request,"account/signup.html",context)