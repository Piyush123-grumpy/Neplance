from django.urls import path
from Homepage import views,accounts


urlpatterns = [
    path('about/', views.about,name='about')
]