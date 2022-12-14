"""Neplance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
import Homepage.views as homepage




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage.home, name='homepage'),
    path('', include('account.urls')),
    path('gig/', include('gig.urls')),
    path('', include('search.urls')),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
    # path('', include('forgotPassword.urls')),
    path('', include('forgotPassword.urls')),
    path('', include('Homepage.urls')),


    path("accounts/", include("django.contrib.auth.urls")),
    path('',include('forgotPassword.urls')),
    path('', include('rating.urls')),
    
    path('khalti/', include('khalti.urls')),
    path('',include('profilePage.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
