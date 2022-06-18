from ast import Add
from django.http import HttpResponse, JsonResponse
from django.db.models import Max
from unicodedata import category
from django.shortcuts import redirect, render
from account.models import User

from gig.models import Application, Category, Gig
from .forms import AddGigForm
from django.contrib.auth.decorators import login_required

import json

# Create your views here.
@login_required(login_url='/login/') # Redirect when user is not logged in.
def addgigs(request):
    # Validate if use is an employer.
    if request.user.is_employer:
        # Executes before form submission.
        if request.method != 'POST':
            form = AddGigForm()
            return render(request,'addgigs.html', {'form': form})

        # Executes after form submission.
        else:
            form = AddGigForm(request.POST)
            # Save form data if the form is valid.
            if form.is_valid:
                f = form.save()
                f.user = request.user # Set user to current user.
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
    return render(request, 'jobdetail.html', {'jobdetail': jobdetail})

def joblist(request):
    return render(request, 'joblist.html', {'jobs': Gig.objects.all})

def applyJob(request):
        # Stuts code meanings:
# <---------------------------------------------------> #
        # 0: Default status.
            # 420: User doesn't exist.
                # 69: Gig doesn't exist.
                    # 69420: Application already exists.
                        # 6969: Application saved.
                            # 9999: Recieved Get request.

    if request.method == 'POST':
        # userid = request.POST['user']
        # gigid = request.POST['gig']
        # print('------------------------------------------')
        # print('user: ', userid, ' gig: ', gigid)
        # print('------------------------------------------')
        print('posted data:::::::::', str(request.POST['user']))


# 5:20 6-18-2020 Update: validationi working properly. Views working all good
# But data not pasing through javascript.





# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     # credential validation

    #     # if user doesn't exists.
    #     if not User.objects.filter(id = userid).exists():
    #         return JsonResponse(420, safe=False)

    #     # if gig doesn't exist.
    #     elif not Gig.objects.filter(id = gigid).exists():
    #         return JsonResponse(69, safe=False)


    #     user = User.objects.get(id = userid)
    #     gig = Gig.objects.get(id = gigid)

        

    #     # if application already exists.
    #     if Application.objects.filter(user=user, gig=gig).exists():
    #         return JsonResponse(69420, safe=False)
    #     # If all criterias are fulfilled.
    #     else:
    #         # save application.
    #         # application = Application()
    #         # application.user = user
    #         # application.gig = gig
    #         # application.save()
    #         return JsonResponse(6969, safe=False)
    # else:
        return JsonResponse(9999, safe=False)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# <---------------------------------------------------> #
#                      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⣀⣀⣠⡴⠶⣄⠀⢀⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
#              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣄⠀⠹⠤⠃⠀⡏⠉⠉⠳⢾⡿⣻⡆⠀⠀⠀⠀⠀⠀⠀⠀ 
#              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠇⠀⠀⠀⣠⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
#              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣴⡀⡀⠀⣴⣆⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
#              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣷⣷⣷⣶⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
#              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⡿⢻⣿⢻⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
#              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠏⠜⠀⠈⢉⣿⡟⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
#              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠁⠀⠀⠀⠀⠀⠉⠁⠈⢻⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
#              ⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⢀⣤⣄⠀⠀⠀⠀⠣⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀ 
#              ⠀⠀⠀⠀⠀⠀⣰⠟⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠰⠂⠙⣦⠀⠀⠀⠀⠀⠀ 
#              ⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣶⣤⡀⠀⠀⠐⣂⠈⢳⡄⠀⠀⠀⠀ 
#              ⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⣴⣿⣿⡿⣿⣿⣿⠿⣿⣿⣿⣆⠀⠀⠰⢒⠵⢻⣆⠀⠀⠀ 
#              ⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⣿⣿⣿⠀⠈⢿⣿⣿⠄⠀⠀⠄⢊⡡⠜⣦⠀⠀ 
#              ⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣷⣿⣿⣿⠀⠀⠈⠙⠉⠀⠀⠀⢒⡡⠔⣋⠼⡇⠀ 
#              ⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣷⣶⣄⠀⠀⠀⠀⠀⠐⣈⠤⠒⢻⡄ 
#              ⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣟⠛⢿⣿⣿⣷⠀⠀⠀⠐⣉⠤⠒⣉⠬⣇ 
#              ⢸⠇⢀⠀⠀⠀⠀⠀⠀⣠⣤⡀⠀⠀⣿⣿⣿⠀⠀⣹⣿⣿⡇⠀⠀⡈⠤⠒⣉⠤⠀⣿ 
#              ⢸⠀⠘⣆⡀⠀⠀⠀⠀⢿⣿⣿⣄⠀⣿⣿⣿⢀⣴⣿⣿⡿⠀⠀⠀⠤⠒⣉⠤⠒⠀⡿ 
#              ⢸⡆⢰⡆⠁⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠀⠀⠀⠠⢒⣉⠤⠒⠁⣸⠃ 
#              ⠀⢳⡀⠙⠒⢷⣀⠀⠀⠀⠀⠈⠛⠻⣿⣿⣿⠛⠉⠀⠀⠀⠀⠐⢊⣁⠤⠒⠋⣠⠏⠀ 
#              ⠀⠀⠳⣤⣧⡀⠸⡀⠀⠀⠀⠀⠀⠀⠻⣿⠟⠀⠀⠀⠀⠀⠔⣊⡡⠤⠒⢉⡴⠋⠀⠀ 
#              ⠀⠀⠀⠀⠙⠳⠦⣌⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣁⣤⣴⡾⠟⠋⠀⠀⠀⠀ 
#              ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠒⠒⠶⠦⠤⠤⠤⠴⠶⠒⠒⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀ 
# <---------------------------------------------------> #