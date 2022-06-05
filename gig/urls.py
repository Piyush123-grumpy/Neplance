from django.urls import path
from gig import views


urlpatterns = [
        path('addgig/', views.addgigs, name='addgig'),
        path('search/', views.search, name = 'search'),
        path('filtersearch/<int:category>/<int:min>/<int:max>', views.filterSearch, name='filterSearch'),
]
