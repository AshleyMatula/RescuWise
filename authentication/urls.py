from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from authentication.views import *

urlpatterns = [
    # Admin Urls
    path('admin/', admin.site.urls),

    # allauth urls
    path('accounts/', include('allauth.urls')),

    # General UI
    path('accounts/dashboard/', DashboardView.as_view(), name='dashboard'),
]
