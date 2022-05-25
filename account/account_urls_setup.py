from django.urls import path
from account import views,accounts



urlpatterns = [
    path('/freelancer_Save',views.Freelancer_info_save,name='Freelancer_info_save'),
]