from multiprocessing import context
from django.shortcuts import render
from account.forms import freelancer

from account.models import Freelancer, Other_experience, User, employment_history, portfolio

# Create your views here.

def profileer(request):
    return render(request,'profiless.html')

def profileer(request,id):
    user=User.objects.get(id=id)
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
    return render(request,'profiless.html',context)

def lol(request):
    user=User.objects.all().order_by('-id')
    freelancer=Freelancer.objects.all()
    context={
        'user':user,
        'freelancer':freelancer
    }
    return render(request,'lol.html',context)