from django.http import HttpResponse
from django.shortcuts import render,redirect 


def account_detail(request):
    return render(request,'account/account_detail.html')