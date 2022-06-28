from django.urls import path
from profilePage import views
from rating import views as rating

urlpatterns = [
    path('pro/<int:id>/',views.profileer,name="profiles"),
    path('pro',views.lol,name="lol"),
    path('submit_review/<int:freelancer_id>',rating.submit_review,name="submit_review"),
]
