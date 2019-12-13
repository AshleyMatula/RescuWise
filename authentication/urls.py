from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from authentication.views import *

urlpatterns = [
    # Admin Urls
    path('admin/', admin.site.urls),
    
    # allauth urls
    path('accounts/', include('allauth.urls')),

    # Login and Auth Views 
    # path('signup/', SignUp.as_view(), name="signup"),
    # path('login/', Login.as_view(), name="login"),
    # path('logout/', Logout.as_view(), name="logout"),
    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    # path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    # path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    # path('access_resource_error/', TemplateView.as_view(template_name="access_resource_error.html")),

    # General UI
    path('accounts/dashboard/', DashboardView.as_view(), name='dashboard'),
]