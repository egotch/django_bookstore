"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import settings
from django.contrib import admin
from django.urls import path, include
import django.contrib.auth.views as auth_views

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    # User Management
    # path('logout/', auth_views.LogoutView.as_view(next_page=settings.ACCOUNT_LOGOUT_REDIRECT ), name='logout'),
    path("accounts/", include("allauth.urls")),
    # Local Apps
    # path("accounts/", include("accounts.urls")),
    path("", include("pages.urls")),
]
