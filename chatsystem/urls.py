from django.urls import path
from . import views

urlpatterns = [
    path('chatlist',views.chatlist,name="chat page"),
    path('create_session/<str:name>',views.create_session,name="create session"),
    path('chat/<str:name>',views.chat,name="chat"),
    path('get_message/<str:name>',views.get_message,name="get message"),
    path('send',views.send,name="send"),
    
]
