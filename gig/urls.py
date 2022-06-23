from django.urls import path
from gig import views


urlpatterns = [
        path('addgig/', views.addgigs, name='addgig'),
        path('search/', views.search, name = 'search'),
        path('filtersearch/<int:category>/<int:min>/<int:max>', views.filterSearch, name='filterSearch'),
        path('jobdetail/<int:job>', views.jobdetail,name='jobdetail'),
        path('joblist/', views.joblist, name='joblist'),
        path('applyjson/', views.applyJob, name='applyJson'),
        path('postedgigs/', views.postedGigs, name='postedGigs'),
        path('applicationlist/<int:gigid>', views.applicationList, name='applicationlist'),
        path('removeGig/', views.removeGig, name='removeGig'),
]
