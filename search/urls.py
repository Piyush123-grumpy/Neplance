from django.urls import path
from .views import categoryPage

urlpatterns = [
        path('', categoryPage, name='category'),
]