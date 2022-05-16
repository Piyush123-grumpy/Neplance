from django.urls import path
from account import views


urlpatterns = [
    path('', views.home,name='home'),
    path('register/', views.register,name='register'),
    path('signup_freelancer/',views.signup_freelancer,name='signup_freelancer'),
    path('signup_employer/',views.signup_employer,name='signup_employer'),
    path('login/', views.loginpage,name='login_dashboard'),
]