from django.shortcuts import render

# Create your views here.
def addgigs(request):
    return render(request,'account/addgigs.html')