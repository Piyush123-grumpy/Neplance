from django.urls import path
from account import views


urlpatterns = [
    path('', views.home,name='home'),
    path('register/', views.register,name='register'),
    path('signup/',views.signup,name='signup')
]