from django.shortcuts import redirect, render

from account.forms import freelancer
from rating.forms import ReviewForm
from .models import Employer, Freelancer,ReviewRating
# Create your views here.
def rating(request):
    freelancer=Freelancer.objects.get(user_id=2)
    context={"freelancer":freelancer}
    return render(request,'rate.html',context)

def submit_review(request,freelancer_id):
    print(freelancer_id)
    url=request.META.get('HTTP_REFERER')
    try:
        review= ReviewRating.objects.get(employer__user_id=request.user.id,freelancer__user_id=freelancer_id)
        form=ReviewForm(request.POST,instance=review)
        form.save()
        return redirect(url)      
    except ReviewRating.DoesNotExist:
        form=ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(url)