from django.shortcuts import render

# Create your views here.

def home(request):
    print(request.user)
    return render(request, 'base/homepage.html')

def about(request):
    # print(request.user)
    return render(request, 'base/about.html')