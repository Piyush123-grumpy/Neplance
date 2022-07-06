from django.urls import path
from .views import searchPage

urlpatterns = [
        path('search/', searchPage, name='category'),
]