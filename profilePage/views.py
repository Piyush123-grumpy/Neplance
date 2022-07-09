from multiprocessing import context
from django.shortcuts import redirect, render
from account.forms import freelancer
from django.db.models import Sum
from account.models import Freelancer, Other_experience, User, employment_history, portfolio
from rating.models import ReviewRating
from django.contrib.auth.decorators import login_required

# Create your views here.

def profileer(request):
    return render(request,'profiless.html')
@login_required(login_url='/login/')
def profileer(request,id):
    if request.user.is_employer:
        try:
            print(id)
            freelancer=Freelancer.objects.filter(user_id=id)[0]
            sum=ReviewRating.objects.filter(freelancer_id=freelancer).aggregate(Sum('rating'))
            number=ReviewRating.objects.filter(freelancer_id=freelancer).count()  
            avg_rating=sum["rating__sum"]/number
            print(freelancer)
            Portfolio=portfolio.objects.filter(freelancer=freelancer)
            Employment=employment_history.objects.filter(freelancer=freelancer)
            other_exp=Other_experience.objects.filter(freelancer=freelancer)
            context={
                'freelancer':freelancer,
                'portoflio':Portfolio,
                'Employment':Employment,
                'other_exp':other_exp,
                "avg_rating":avg_rating}
            return render(request,'profiless.html',context)
        except TypeError:
            freelancer=Freelancer.objects.filter(user_id=id)[0]
            Portfolio=portfolio.objects.filter(freelancer=freelancer)
            Employment=employment_history.objects.filter(freelancer=freelancer)
            other_exp=Other_experience.objects.filter(freelancer=freelancer)
            context={
                'freelancer':freelancer,
                'portoflio':Portfolio,
                'Employment':Employment,
                'other_exp':other_exp,}
            return render(request,'profiless.html',context)
    else:
        return redirect('/')


def rating(request):
    freelancer=Freelancer.objects.get(user_id=2)
    sum=ReviewRating.objects.filter(freelancer_id=2).aggregate(Sum('rating'))
    number=ReviewRating.objects.filter(freelancer_id=2).count()   
    avg_rating=sum["rating__sum"]/number
    context={"freelancer":freelancer,"avg_rating":avg_rating}
    return render(request,'rate.html',context)




def lol(request):
    user=User.objects.all().order_by('-id')
    freelancer=Freelancer.objects.all()
    context={
        'user':user,
        'freelancer':freelancer
    }
    return render(request,'lol.html',context)