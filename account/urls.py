from django.urls import path
from account import views


urlpatterns = [
    path('', views.register,name='home'),
]