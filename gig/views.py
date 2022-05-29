from django.shortcuts import render

# Create your views here.
def addgigs(request):
    print(request.user.is_authenticated)
    # if request.user.is_hirer:
    return render(request,'addgigs.html')