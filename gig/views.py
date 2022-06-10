from ast import Add
from django.http import HttpResponse, JsonResponse
from django.db.models import Max
from unicodedata import category
from django.shortcuts import redirect, render

from gig.models import Category, Gig
from .forms import AddGigForm
from django.contrib.auth.decorators import login_required

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
    print(Gig.objects.filter(pay__range=[10000,20000]))
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

def jobdetail(request):
    return render(request, 'jobdetail.html')
