from ast import Add
from datetime import datetime
from django.http import HttpResponse, JsonResponse, QueryDict
from django.db.models import Max
from unicodedata import category, name
from django.shortcuts import redirect, render
from account.models import Employer, Freelancer, User

from gig.models import Application, Category, Gig, Requirement
from .forms import AddGigForm
from django.contrib.auth.decorators import login_required

import json

# Create your views here.
@login_required(login_url='/login/')
def addgigs(request):
    
    # Validate if use is an employer.
    if request.user.is_employer:
        # Executes before form submission.
        if request.method != 'POST':
            form = AddGigForm()
            return render(request,'addgigs.html', {'form': form})

        # Executes after form submission.
        else:
            employer=Employer.objects.get(id=request.user.id)
            form = AddGigForm(request.POST)
            # Save form data if the form is valid.
            if form.is_valid:
                f = form.save()
                f.Employer = employer  # Set user to current user.
                f.save()
                print('saved gig') # Print alert message.
                return redirect('/')
            return render(request,'addgigs.html', {'form': form})

    # If user is not logged in redirect to home page.
    else:
        return redirect('/')

def search(request):
    categories = Category.objects.all
    context = {'categories': categories}
    return render(request, 'search.html', context)

def filterSearch(request, category, min, max):
    data = None

    data = list(Gig.objects.values().filter(category = category, pay__range=[min, max]))
    # If only Max value is given.
    if min == -9999 and max != -9999:
        min = 0
        # data = list(Gig.objects.values().filter(category = category, pay__range=[0, max]))
    # If only Min value is given.
    elif max == -9999 and min != -9999:
        max = Gig.objects.aggregate(Max('pay'))
        # data = list(Gig.objects.values().filter(category = category, pay__range=[min, Gig.objects.aggregate(Max('pay'))]))
    # If category not given.
    if category == -9999:
        data = list(Gig.objects.values().filter(pay__range=[min, max]))
    else:
        data = list(Gig.objects.values().filter(category = category, pay__range=[min, max]))
    return JsonResponse(data, safe=False)

def jobdetail(request, job):
    jobdetail = Gig.objects.get(id=job)
    
    user = request.user
    if user.is_freelancer:
        freelancer=Freelancer.objects.get(user_id=user)
        if request.user.is_authenticated:
            exists = Application.objects.filter(Freelancer=freelancer, gig=job).exists()
            return render(request, 'jobdetail.html', {'jobdetail': jobdetail, 'user': user, 'exists': exists})
        else:
            return render(request, 'jobdetail.html', {'jobdetail': jobdetail, 'user': user})
    else:
        return render(request, 'jobdetail.html', {'jobdetail': jobdetail, 'user': user})

def joblist(request):
    return render(request, 'joblist.html', {'jobs': Gig.objects.all})

def applyJob(request):
# <--------------- STATUS CODE MEANINGS ---------------> #
        # 0: Default status.
            # 420: User doesn't exist.
                # 69: Gig doesn't exist.
                    # 69420: Application already exists.
                        # 6969: Application saved.
                            # 9999: Recieved Get request.
# <--------------- STATUS CODE MEANINGS ---------------> #

# VALIDATIONS
    # If recieves POST request.
    if request.method == 'POST':
        # Recieves QueryDict. Convert to python dict.
        data = QueryDict.dict(request.POST)
        # Recieves data in str format. Parse to int.
        userid = int(data['user'])
        gigid = int(data['gig'])
        employer= int(data['employer'])
        print(userid)
        print(gigid)
        print(employer)

    # CREDENTIALS VALIDATION

        # If user doesn't exists.
        if not Freelancer.objects.filter(user_id = userid).exists():
            print("exist wala error")
            return JsonResponse(420, safe=False)

        # If gig doesn't exist.
        elif not Gig.objects.filter(id = gigid).exists():
            print("gig nava error")
            return JsonResponse(69, safe=False)

        freelancer = Freelancer.objects.get(user_id = userid)
        gig = Gig.objects.get(id = gigid)
        employa=Employer.objects.get(id=employer)

        # If application already exists.
        if Application.objects.filter(Freelancer=freelancer, gig=gig).exists():
            print("App vako error")
            return JsonResponse(69420, safe=False)

        # If all criterias are fulfilled.
        else:
            # Save application.
            application = Application()
            application.Freelancer = freelancer
            application.Employer = employa
            application.gig = gig
            application.save()
            return JsonResponse(6969, safe=False)
    # If recieves GET request.
    else:
        return JsonResponse(9999, safe=False)

def postedGigs(request):
    if request.user.is_employer:
        gigs = Gig.objects.filter(Employer = request.user.id)
        return render(request, 'postedjobs.html', {'gigs':gigs})
    else:
        return redirect('/')

def applicationList(request, gigid):
    if request.user.is_employer:
        gig = Gig.objects.get(id=gigid)
        employer=Employer.objects.get(user_id=request.user.id)
        applications = Application.objects.filter(Employer=employer,gig=gig)
        return render(request, 'applicationlist.html', {'applications':applications})

    return redirect('/')

def removeGig(request):
    gigid = request.POST['gig']
    exists = Gig.objects.filter(id=gigid).exists()
    if exists:
        Gig.objects.get(id=gigid).delete()
        return JsonResponse(69, safe=False)
    else:
        return JsonResponse(420, safe=False)

@login_required(login_url='/login/')
def updateApplicationStat(request):
    if request.method=="POST":
        if request.user.is_employer:
            appId = request.POST['application']
            status = request.POST['status']
            if Application.objects.filter(id=appId).exists():
                app = Application.objects.get(id=appId)
                if status == "Rejected":
                    app.status="Rejected"
                    app.save()
                    return JsonResponse("Updated", safe=False)
                elif status == "Hired":
                    app.employer_paid = True
                    app.status="Hired"
                    app.save()
                    return JsonResponse("Updated", safe=False)
                elif status == "Pending Completed":
                    app.status="Pending Completed"
                    app.save()
                    return JsonResponse("Updated", safe=False)
                elif status == "Completed":
                    app.status="Completed"
                    app.save()
                    return JsonResponse("Updated", safe=False)
                else:
                    return JsonResponse("Invalid Status: ",status , safe=False)
            else:
                return JsonResponse("Application doesn't exist.", safe=False)
    else:
        return JsonResponse("Invalid Method.", safe=False)
    
def userapplicationlist(request):
    applications = Application.objects.filter(Freelancer=Freelancer.objects.get(user=request.user))

    Jobs = Gig.objects.filter()
    return render(request,'applicationlist.html', {'applications': applications})

