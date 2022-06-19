from django.urls import path
from account import views,accounts


urlpatterns = [
    path('register/', views.register,name='register'),
    path('signup_freelancer/',views.signup_freelancer,name='signup_freelancer'),
    path('signup_employer/',views.signup_employer,name='signup_employer'),
    path('login/', views.loginpage,name='login_dashboard'),
    
    path('profile/', accounts.editUser,name='editUser'),
    path('account_detail',accounts.account_detail,name='account_detail'),
    path('freelancer_Save',accounts.Freelancer_info_save,name='Freelancer_info_save'),
    path('portfolio',accounts.Portoflio,name='Portfolio'),
    path('save_portfolio',accounts.save_protfolio,name='Save_Portfolio'),
    path('employment_history',accounts.Employment_history,name='Employment_history'),
    path('save_employment_history',accounts.save_employment_history,name='save_employment_history'),
    path('other_experience',accounts.other_experience,name='other_experience'),
    path('save_other_experience',accounts.save_other_experience,name='save_other_experience'),
    
    
    path('reviews/', views.reviews,name='reviews'),
    path('appliedjobs/', views.appliedJobs,name='appliedJobs'), 

]