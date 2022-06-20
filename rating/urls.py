from django.urls import path
from rating import views

urlpatterns = [
    path('rating',views.rating,name="rating"),
    path('submit_review/<int:freelancer_id>',views.submit_review,name="submit_review"),
    path('review',views.review,name="review")
]