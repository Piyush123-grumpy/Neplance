from django.urls import path
from profilePage import views

urlpatterns = [
    path('pro/<int:id>/',views.profileer,name="profiles"),
    path('pro',views.lol,name="lol")
]