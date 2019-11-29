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


from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    # include core app urls (static/non-auth pages)
    path('', include('core.urls')),

    # include shelters app urls
    path('', include('shelters.urls')),

    # include animals app urls
    path('', include('animals.urls')),

    # include authentication urls
    path('', include('authentication.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
