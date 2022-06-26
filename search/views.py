from turtle import title
from django.shortcuts import render

from gig.models import Category, Gig

# Create your views here.
# def searchPage(request):
#     # tag, category, max_price, min_price
#     print('path::::: ' + request.path)
#     filters = Gig.objects.all()
#     if 'category' in request.GET:
#         category = request.GET['category']
#         print('GOT category')
#         if Category.objects.filter(category_name=category).exists():
#             category = Category.objects.get(category_name=category)
#             filters.filter(category=category)
#             print("CATEGORY EXISTS")
#     if 'country' in request.GET:
#         country = request.GET['country']
#         filters.filter(country=country)
#         print("COUNTRY EXISTS")
#             # return render(request, 'category.html', {'gigs': gigs})
#     return render(request, 'category.html', {'gigs': filters})
#     # return render(request, 'category.html', {'category': category})


def searchPage(request):
    gigs = Gig.objects.all()
    categories = Category.objects.all()

    
    if 'category' in request.GET:
        category = Category.objects.get(category_name=request.GET['category'])
        gigs = gigs.filter(category=category)

    if 'country' in request.GET:
        gigs = gigs.filter(country__name=request.GET['country'])
    
    if 'tag' in request.GET:
        gigs1 = gigs.filter(title__icontains=request.GET['tag'])
        gigs2 = gigs.filter(company__icontains=request.GET['tag'])
        gigs=gigs1|gigs2

    # Price Filter
    if ('min' in request.GET) and ('max' in request.GET):
        print('GOT BOTH')
        min = request.GET['min']
        max = request.GET['max']
        gigs = gigs.filter(pay__range=[min, max])
    elif ('min' in request.GET) and (not 'max' in request.GET):
        print("GOT MINNNN")
        min = int(request.GET['min'])
        gigs = gigs.filter(pay__gte = min)
        print(type(min))
    elif not ('min' in request.GET) and ('max' in request.GET):
        max = int(request.GET['max'])
        print(type(max))
        gigs = gigs.filter(pay__lte = max)

    return render(request, 'category.html', {'gigs': gigs, 'categories':categories})