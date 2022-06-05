from django.urls import path
from gig import views


urlpatterns = [
        path('addgig/', views.addgigs,name='addgig'),
        path('jobdetail/', views.jobdetail,name='jobdetail'),
]
