from django.urls import path
from Homepage import views


urlpatterns = [
path('about/', views.about,name='about')
]