from django.urls import path
from gig import views


urlpatterns = [
<<<<<<< HEAD
        path('addgig/', views.addgigs, name='addgig'),
        path('search/', views.search, name = 'search'),
        path('filtersearch/<int:category>/<int:min>/<int:max>', views.filterSearch, name='filterSearch'),
=======
        path('addgig/', views.addgigs,name='addgig'),
        path('jobdetail/', views.jobdetail,name='jobdetail'),
>>>>>>> origin/gig-frontend
]
