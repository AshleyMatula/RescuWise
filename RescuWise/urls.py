"""RescuWise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from RescuWise.views import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('animals/', AnimalIndex.as_view(), name='animals'),
    path('admin/', admin.site.urls),
    # Login and Auth Views #
    path('signup/', SignUp.as_view(), name="signup"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('access_resource_error/',TemplateView.as_view(template_name="access_resource_error.html")),
    path('access_resource_error/',TemplateView.as_view(template_name="access_resource_error.html")),

    # action urls
    path('createanimal/',CreateAnimal.as_view()),
    path('listanimals/',ListAnimals.as_view()),
    path('createshelter/',CreateShelter.as_view()),
    path('listshelters/',ListShelters.as_view()),

    # catch alls
    path('', Home.as_view()),
    path('<template_name>/', DynamicStaticPages.as_view()),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
