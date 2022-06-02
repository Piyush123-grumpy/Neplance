from ast import Add
from django.shortcuts import redirect, render
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